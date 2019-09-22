# coding=utf-8

import os
import collections
from lxml import etree

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from unittest import TestCase
from requests import Session
from erpbrasil.assinatura.certificado import Certificado
from erpbrasil.transmissao import TransmissaoSOAP
from erpbrasil.assinatura.certificado import ArquivoCertificado

Requisicao = collections.namedtuple(
    'Requisicao', ['apelido', 'url', 'operacao', 'xml', 'header']
)

nfe = Requisicao(
    'nfe',
    'https://hom.sefazvirtual.fazenda.gov.br/NFeStatusServico4/NFeStatusServico4.asmx?wsdl',
    # noqa
    'nfeStatusServicoNF',
    """<consStatServ xmlns="http://www.portalfiscal.inf.br/nfe" versao="4.00"><tpAmb>2</tpAmb><cUF>35</cUF><xServ>STATUS</xServ></consStatServ>""",
    # noqa
    False
)
cte = Requisicao(
    'cte',
    'https://homologacao.nfe.fazenda.sp.gov.br/cteWEB/services/CteStatusServico.asmx?WSDL',
    # noqa
    'cteStatusServicoCT',
    """<consStatServCte xmlns="http://www.portalfiscal.inf.br/cte" versao="3.00"><tpAmb>2</tpAmb><xServ>STATUS</xServ></consStatServCte>""",
    # noqa
    True
)

gnre = Requisicao(
    'gnre',
    'https://www.testegnre.pe.gov.br/gnreWS/services/GnreConfigUF?wsdl',
    'consultar',
    '<TConsultaConfigUf xmlns="http://www.gnre.pe.gov.br"><ambiente>2</ambiente><uf>CE</uf><receita courier="N">100056</receita></TConsultaConfigUf>',
    True,
)

mdfe = Requisicao(
    'mdfe',
    'https://mdfe-homologacao.svrs.rs.gov.br/ws/MDFeStatusServico/MDFeStatusServico.asmx?WSDL',
    'mdfeStatusServicoMDF',
    """<consStatServMDFe xmlns="http://www.portalfiscal.inf.br/mdfe" versao="3.00"><tpAmb>2</tpAmb><xServ>STATUS</xServ></consStatServMDFe>""",
    # noqa
    True,
)


class Tests(TestCase):
    """ Rodar este teste muitas vezes pode bloquear o seu IP"""

    def setUp(self):
        certificado_nfe_caminho = os.environ.get(
            'certificado_nfe_caminho',
            'tests/teste.pfx'
        )
        certificado_nfe_senha = os.environ.get(
            'certificado_nfe_senha', 'teste'
        )
        self.certificado = Certificado(certificado_nfe_caminho,
                                  certificado_nfe_senha)

    def test_nfe(self):
        with ArquivoCertificado(self.certificado, 'w') as (key, cert):
            session = Session()
            session.cert = (key, cert)
            session.verify = False
            transmissao = TransmissaoSOAP(self.certificado, session)

            #
            # NFE
            #

            cliente = transmissao.cliente(nfe.url)
            xml = etree.fromstring(
                nfe.xml,
                parser=etree.XMLParser()
            )
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
            with cliente.settings(raw_response=True):
                resposta = cliente.service[nfe.operacao](xml)
                self.assertTrue(resposta.ok)
                print(resposta.text)

    def test_cte(self):
        with ArquivoCertificado(self.certificado, 'w') as (key, cert):
            session = Session()
            session.cert = (key, cert)
            session.verify = False
            transmissao = TransmissaoSOAP(self.certificado, session)
            #
            # CTE
            #

            cliente = transmissao.cliente(cte.url)
            if cte.header:
                header_element = cliente.get_element('ns0:cteCabecMsg')
                header = header_element(
                    cUF='35',
                    versaoDados='3.00'
                )
                cliente.set_default_soapheaders([header])

            xml = etree.fromstring(
                cte.xml,
                parser=etree.XMLParser()
            )
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
            with cliente.settings(raw_response=True):
                resposta = cliente.service[cte.operacao](xml)
                self.assertTrue(resposta.ok)
                print(resposta.text)

    # def test_gnre(self):
    #
    # with ArquivoCertificado(self.certificado, 'w') as (key, cert):
    #     session = Session()
    #     session.cert = (key, cert)
    #     session.verify = False
    #     transmissao = TransmissaoSOAP(self.certificado, session)
    #
    # GNRE
    #
    # Esse teste esta muito complicado, devido aos certificados defeituosos
    # do servidor,
    # session.verify = True

    # tentei setar os certificados

    # os.environ['REQUESTS_CA_BUNDLE'] = '/home/mileo/Projects/oca10/src/erpbrasil.transmissao/tests/certificados/www_testegnre_pe_gov_br.pem'

    # https://2.python-requests.org//en/latest/user/advanced/
    # https://stackoverflow.com/questions/30405867/how-to-get-python-requests-to-trust-a-self-signed-ssl-certificate
    # https://groups.google.com/forum/#!msg/nfephp/vGaomO5sMXo/PBw4TAKatIoJ
    # https://github.com/nfephp-org/sped-gnre
    # http://www.gnre.pe.gov.br/gnre/portal/faq.jsp

    # Alem disso atualizei todos os certicados AC do Brasil + os da GNRE no
    # diretório de certificados do linux, mas não resolveu.
    # session.merge_environment_settings(gnre.url, {}, None, None, None)
    #

    # cliente = transmissao.cliente(gnre.url)
    # if gnre.header:
    #     header_element = cliente.get_element('ns0:gnreCabecMsg')
    #     header = header_element(
    #         versaoDados='1.00'
    #     )
    #     cliente.set_default_soapheaders([header])
    #
    # xml = etree.fromstring(
    #     gnre.xml,
    #     parser=etree.XMLParser()
    # )
    # requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    # with cliente.settings(raw_response=True):
    #     resposta = cliente.service[gnre.operacao](xml)
    #     print(resposta.text)

    def test_mdfe(self):
        with ArquivoCertificado(self.certificado, 'w') as (key, cert):
            session = Session()
            session.cert = (key, cert)
            session.verify = False
            transmissao = TransmissaoSOAP(self.certificado, session)
            #
            # MDFE
            #

            cliente = transmissao.cliente(mdfe.url)
            if cte.header:
                header_element = cliente.get_element('ns0:mdfeCabecMsg')
                header = header_element(
                    cUF='35',
                    versaoDados='3.00'
                )
                cliente.set_default_soapheaders([header])

            xml = etree.fromstring(
                mdfe.xml,
                parser=etree.XMLParser()
            )
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
            with cliente.settings(raw_response=True):
                resposta = cliente.service[mdfe.operacao](xml)
                self.assertTrue(resposta.ok)
                print(resposta.text)


t = Tests()
t.setUp()
t.test_nfe()
t.test_cte()
t.test_mdfe()
