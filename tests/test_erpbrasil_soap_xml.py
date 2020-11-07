# coding=utf-8

import collections
import os
from unittest import TestCase

import vcr
from erpbrasil.assinatura.certificado import Certificado
from requests import Session

from erpbrasil.transmissao import TransmissaoSOAP

Requisicao = collections.namedtuple(
    'Requisicao', ['apelido', 'url', 'operacao', 'xml', 'header']
)

nfe = Requisicao(
    'nfe',
    'https://hom.sefazvirtual.fazenda.gov.br/NFeStatusServico4/NFeStatusServico4.asmx?wsdl',
    # noqa
    'nfeStatusServicoNF',
    """<consStatServ xmlns="http://www.portalfiscal.inf.br/nfe" versao="4.00">
            <tpAmb>2</tpAmb>
            <cUF>35</cUF>
            <xServ>STATUS</xServ>
       </consStatServ>""",
    # noqa
    False
)
cte = Requisicao(
    'cte',
    'https://homologacao.nfe.fazenda.sp.gov.br/cteWEB/services/CteStatusServico.asmx?WSDL',
    # noqa
    'cteStatusServicoCT',
    """
    <consStatServCte xmlns="http://www.portalfiscal.inf.br/cte" versao="3.00">
        <tpAmb>2</tpAmb>
        <xServ>STATUS</xServ>
    </consStatServCte>""",
    # noqa
    True
)

gnre = Requisicao(
    'gnre',
    'https://www.testegnre.pe.gov.br/gnreWS/services/GnreConfigUF?wsdl',
    'consultar',
    """<TConsultaConfigUf xmlns="http://www.gnre.pe.gov.br">
        <ambiente>2</ambiente>
        <uf>CE</uf>
        <receita courier="N">100056</receita>
    </TConsultaConfigUf>""",
    True,
)

mdfe = Requisicao(
    'mdfe',
    'https://mdfe-homologacao.svrs.rs.gov.br/ws/MDFeStatusServico/MDFeStatusServico.asmx?WSDL',
    'mdfeStatusServicoMDF',
    """
<consStatServMDFe xmlns="http://www.portalfiscal.inf.br/mdfe" versao="3.00">
    <tpAmb>2</tpAmb>
    <xServ>STATUS</xServ>
</consStatServMDFe>""",
    # noqa
    True,
)

vcr_cassettes_path = os.environ.get(
    'vcr_cassettes_path',
    'fixtures/vcr_cassettes'
)


class Tests(TestCase):
    """ Rodar este teste muitas vezes pode bloquear o seu IP"""

    def setUp(self):
        certificado_nfe_caminho = os.environ.get(
            'certificado_nfe_caminho',
            'fixtures/dummy_cert.pfx'
        )
        certificado_nfe_senha = os.environ.get(
            'certificado_nfe_senha', 'dummy_password'
        )
        self.certificado = Certificado(
            certificado_nfe_caminho,
            certificado_nfe_senha
        )
        session = Session()
        session.verify = False
        self.transmissao = TransmissaoSOAP(self.certificado, session)

    @vcr.use_cassette(
        vcr_cassettes_path + '/test_erpbrasil_soap_xml/test_nfe.yaml')
    def test_nfe(self):
        with self.transmissao.cliente(nfe.url):
            resposta = self.transmissao.enviar(
                nfe.operacao, nfe.xml
            )
            self.assertTrue(resposta.ok)
            print(resposta.text)

    @vcr.use_cassette(
        vcr_cassettes_path + '/test_erpbrasil_soap_xml/test_cte.yaml')
    def test_cte(self):
        with self.transmissao.cliente(cte.url):
            self.transmissao.set_header(
                elemento='ns0:cteCabecMsg',
                cUF='35',
                versaoDados='3.00'
            )
            resposta = self.transmissao.enviar(
                cte.operacao, cte.xml
            )
            self.assertTrue(resposta.ok)
            print(resposta.text)

    @vcr.use_cassette(
        vcr_cassettes_path + '/test_erpbrasil_soap_xml/test_gnre.yaml')
    def test_gnre(self):
        # Esse teste esta muito complicado, devido aos certificados defeituosos
        # do servidor,
        # session.verify = True
        #
        # tentei setar os certificados
        #
        # os.environ[
        #     'REQUESTS_CA_BUNDLE'] = '/home/mileo/Projects/oca10/src/erpbrasil.transmissao/tests/certificados/www_testegnre_pe_gov_br.pem'

        # https://2.python-requests.org//en/latest/user/advanced/
        # https://stackoverflow.com/questions/30405867/how-to-get-python-requests-to-trust-a-self-signed-ssl-certificate
        # https://groups.google.com/forum/#!msg/nfephp/vGaomO5sMXo/PBw4TAKatIoJ
        # https://github.com/nfephp-org/sped-gnre
        # http://www.gnre.pe.gov.br/gnre/portal/faq.jsp

        # Alem disso atualizei todos os certicados AC do Brasil + os da GNRE no
        # diretório de certificados do linux, mas não resolveu.
        # session.merge_environment_settings(gnre.url, {}, None, None, None)

        pass
        # with self.transmissao.cliente(gnre.url):
        #     self.transmissao.set_header(
        #         elemento='ns0:gnreCabecMsg',
        #         versaoDados='1.00'
        #     )
        #     resposta = self.transmissao.enviar(
        #        gnre.operacao, gnre.xml
        #     )
        #     self.assertTrue(resposta.ok)
        #     print(resposta.text)

    @vcr.use_cassette(
        vcr_cassettes_path + '/test_erpbrasil_soap_xml/test_mdfe.yaml')
    def test_mdfe(self):
        with self.transmissao.cliente(mdfe.url):
            self.transmissao.set_header(
                elemento='ns0:mdfeCabecMsg',
                cUF='35',
                versaoDados='3.00'
            )
            resposta = self.transmissao.enviar(
                mdfe.operacao, mdfe.xml
            )
            self.assertTrue(resposta.ok)
            print(resposta.text)


t = Tests()
t.setUp()
t.test_nfe()
t.test_cte()
t.test_mdfe()
t.test_gnre()
