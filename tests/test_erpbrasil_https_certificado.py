# coding=utf-8

import os
from unittest import TestCase

import vcr
from erpbrasil.assinatura.certificado import Certificado

from erpbrasil.transmissao import TransmissaoSOAP

NFE = 'https://hom.sefazvirtual.fazenda.gov.br/NFeStatusServico4/NFeStatusServico4.asmx?wsdl'  # noqa
GNRE = 'http://www.testegnre.pe.gov.br/gnreWS/services/GnreResultadoLote?wsdl'  # noqa
ESOCIAL = 'https://webservices.producaorestrita.esocial.gov.br/servicos/empregador/enviarloteeventos/WsEnviarLoteEventos.svc?wsdl'  # noqa
REINF = 'https://preprodefdreinf.receita.fazenda.gov.br/WsREINF/RecepcaoLoteReinf.svc'  # noqa
GINFES = 'https://homologacao.ginfes.com.br/ServiceGinfesImpl?wsdl'
CTE = 'https://homologacao.nfe.fazenda.sp.gov.br/cteWEB/services/CteRecepcao.asmx?WSDL'  # noqa
BETHA = 'http://e-gov.betha.com.br/e-nota-contribuinte-ws/nfseWS?wsdl'
CAMPINAS = 'http://issdigital.campinas.sp.gov.br/WsNFe2/LoteRps.jws?wsdl'
CARIOCA = 'https://homologacao.notacarioca.rio.gov.br/WSNacional/nfse.asmx?wsdl'  # noqa
SIMPLISSWEB = 'http://wshomologacao.simplissweb.com.br/nfseservice.svc?singleWsdl'  # noqa
BELEM = 'http://www.issdigitalbel.com.br/WsNFe2/LoteRps.jws?wsdl'
SOROCABA = 'http://issdigital.sorocaba.sp.gov.br/WsNFe2/LoteRps.jws?wsdl'
TERESINA = 'http://www.issdigitalthe.com.br/WsNFe2/LoteRps.jws?wsdl'
UBERLANDIA = 'http://udigital.uberlandia.mg.gov.br/WsNFe2/LoteRps.jws?wsdl'
SAOLUIS = 'http://sistemas.semfaz.saoluis.ma.gov.br/WsNFe2/LoteRps.jws?wsdl'
CAMPO_GRANDE = 'http://issdigital.pmcg.ms.gov.br/WsNFe2/LoteRps.jws?wsdl'
PETROPOLIS = 'https://petropolis.sigiss.com.br/petropolis/ws/sigiss_ws.php?wsdl'
BH = 'https://bhissdigital.pbh.gov.br/bhiss-ws/nfse?wsdl'
MARINGA = 'https://isseteste.maringa.pr.gov.br/ws/?wsdl'

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
        certificado = Certificado(certificado_nfe_caminho,
                                  certificado_nfe_senha)

        self.transmissao = TransmissaoSOAP(certificado)

    @vcr.use_cassette(
        vcr_cassettes_path +
        '/test_erpbrasil_https_certificado/test_conexao_soap.yaml')
    def test_conexao_soap(self):
        with self.transmissao.cliente(NFE) as cliente:
            self.assertTrue(hasattr(cliente.service, 'nfeStatusServicoNF'))

        with self.transmissao.cliente(GNRE) as cliente:
            self.assertTrue(hasattr(cliente.service, 'consultar'))

        with self.transmissao.cliente(ESOCIAL) as cliente:
            self.assertTrue(hasattr(cliente.service, 'EnviarLoteEventos'))

        with self.transmissao.cliente(CTE) as cliente:
            self.assertTrue(hasattr(cliente.service, 'cteRecepcaoLote'))

        with self.transmissao.cliente(CAMPINAS) as cliente:
            self.assertTrue(hasattr(cliente.service, 'consultarNFSeRps'))

        # with self.transmissao.cliente(BELEM) as cliente:
        #     self.assertTrue(hasattr(cliente.service, 'consultarNFSeRps'))

        with self.transmissao.cliente(SOROCABA) as cliente:
            self.assertTrue(hasattr(cliente.service, 'consultarNFSeRps'))

        with self.transmissao.cliente(TERESINA) as cliente:
            self.assertTrue(hasattr(cliente.service, 'consultarNFSeRps'))

        with self.transmissao.cliente(UBERLANDIA) as cliente:
            self.assertTrue(hasattr(cliente.service, 'consultarNFSeRps'))

        with self.transmissao.cliente(SAOLUIS) as cliente:
            self.assertTrue(hasattr(cliente.service, 'consultarNFSeRps'))

        with self.transmissao.cliente(CAMPO_GRANDE) as cliente:
            self.assertTrue(hasattr(cliente.service, 'consultarNFSeRps'))

        with self.transmissao.cliente(GINFES) as cliente:
            self.assertTrue(hasattr(cliente.service, 'RecepcionarLoteRps'))

        with self.transmissao.cliente(CARIOCA) as cliente:
            self.assertTrue(hasattr(cliente.service, 'RecepcionarLoteRps'))

        with self.transmissao.cliente(BH) as cliente:
            self.assertTrue(hasattr(cliente.service, 'RecepcionarLoteRps'))

        with self.transmissao.cliente(SIMPLISSWEB) as cliente:
            self.assertTrue(hasattr(cliente.service, 'RecepcionarLoteRps'))

        with self.transmissao.cliente(MARINGA) as cliente:
            self.assertTrue(hasattr(cliente.service, 'EnviarLoteRps'))
