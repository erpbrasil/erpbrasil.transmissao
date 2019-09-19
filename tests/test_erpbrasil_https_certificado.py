# coding=utf-8

import os
from unittest import TestCase

from erpbrasil.assinatura.certificado import Certificado
from erpbrasil.transmissao import TransmissaoSOAP

NFE = 'https://hom.sefazvirtual.fazenda.gov.br/NFeStatusServico4/NFeStatusServico4.asmx?wsdl'
GNRE = 'http://www.testegnre.pe.gov.br/gnreWS/services/GnreResultadoLote?wsdl'
ESOCIAL = 'https://webservices.consulta.esocial.gov.br/servicos/empregador/consultarloteeventos/WsConsultarLoteEventos.svc?singleWsdl'
REINF = 'https://preprodefdreinf.receita.fazenda.gov.br/WsREINF/RecepcaoLoteReinf.svc'
GINFES = 'https://homologacao.ginfes.com.br/ServiceGinfesImpl?wsdl'
CTE = 'https://homologacao.nfe.fazenda.sp.gov.br/cteWEB/services/CteRecepcao.asmx?WSDL'


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
            self.transmissao.cliente(GINFES).service, 'RecepcionarLoteRps')
        )
        self.assertTrue(hasattr(
            self.transmissao.cliente(CTE).service, 'cteRecepcaoLote')
        )
