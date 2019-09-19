# coding=utf-8

import os
from unittest import TestCase

from erpbrasil.assinatura.certificado import Certificado
from erpbrasil.transmissao import TransmissaoSOAP

NFE = 'https://hom.sefazvirtual.fazenda.gov.br/NFeStatusServico4/NFeStatusServico4.asmx?wsdl'  # noqa
GNRE = 'http://www.testegnre.pe.gov.br/gnreWS/services/GnreResultadoLote?wsdl'  # noqa
ESOCIAL = 'https://webservices.consulta.esocial.gov.br/servicos/empregador/consultarloteeventos/WsConsultarLoteEventos.svc?singleWsdl'  # noqa
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



class Tests(TestCase):

    def setUp(self):
        certificado_nfe_caminho = os.environ.get(
            'certificado_nfe_caminho',
            'tests/teste.pfx'
        )
        certificado_nfe_senha = os.environ.get(
            'certificado_nfe_senha', 'teste'
        )
        certificado = Certificado(certificado_nfe_caminho,
                                  certificado_nfe_senha)

        self.transmissao = TransmissaoSOAP(certificado)

    def test_conexao_soap(self):
        self.assertTrue(hasattr(
            self.transmissao.cliente(NFE).service, 'nfeStatusServicoNF')
        )
        self.assertTrue(hasattr(
            self.transmissao.cliente(GNRE).service, 'consultar')
        )
        self.assertTrue(hasattr(
            self.transmissao.cliente(ESOCIAL).service, 'ConsultarLoteEventos')
        )
        self.assertTrue(hasattr(
            self.transmissao.cliente(CTE).service, 'cteRecepcaoLote')
        )
        self.assertTrue(hasattr(
            self.transmissao.cliente(CAMPINAS).service, 'consultarNFSeRps')
        )
        self.assertTrue(hasattr(
            self.transmissao.cliente(BELEM).service, 'consultarNFSeRps')
        )
        self.assertTrue(hasattr(
            self.transmissao.cliente(SOROCABA).service, 'consultarNFSeRps')
        )
        self.assertTrue(hasattr(
            self.transmissao.cliente(TERESINA).service, 'consultarNFSeRps')
        )
        self.assertTrue(hasattr(
            self.transmissao.cliente(UBERLANDIA).service, 'consultarNFSeRps')
        )
        self.assertTrue(hasattr(
            self.transmissao.cliente(SAOLUIS).service, 'consultarNFSeRps')
        )
        self.assertTrue(hasattr(
            self.transmissao.cliente(UBERLANDIA).service, 'consultarNFSeRps')
        )
        self.assertTrue(hasattr(
            self.transmissao.cliente(CAMPO_GRANDE).service, 'consultarNFSeRps')
        )
        self.assertTrue(hasattr(
            self.transmissao.cliente(GINFES).service, 'RecepcionarLoteRps')
        )
        self.assertTrue(hasattr(
            self.transmissao.cliente(CARIOCA).service, 'RecepcionarLoteRps')
        )
        self.assertTrue(hasattr(
            self.transmissao.cliente(BH).service, 'RecepcionarLoteRps')
        )
        self.assertTrue(hasattr(
            self.transmissao.cliente(SIMPLISSWEB).service, 'RecepcionarLoteRps')
        )
        self.assertTrue(hasattr(
            self.transmissao.cliente(MARINGA).service, 'EnviarLoteRps')
        )
        # print(dir(self.transmissao.cliente(PETROPOLIS).service))

