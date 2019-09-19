# coding=utf-8
# Copyright (C) 2019  Luis Felipe Mileo - KMEE

import abc

from erpbrasil.assinatura.certificado import ArquivoCertificado
from erpbrasil.assinatura.certificado import Certificado
from requests import Session
from zeep import Client
from zeep.transports import Transport

ABC = abc.ABCMeta('ABC', (object,), {})


class Transmissao(ABC):
    """
    Classe abstrata responsavel por definir os metodos e logica das classes
    de transmissao com os webservices.
    """
    @abc.abstractmethod
    def post(self):
        pass


class TransmissaoSOAP(Transmissao):

    def __init__(self, certificado):
        self.certificado = certificado

    def post(self):
        pass

    def cliente(self, url, verify=False):
        with ArquivoCertificado(self.certificado, 'w') as (key, cert):
            session = Session()
            session.cert = (cert, key)
            session.verify = verify
            transport = Transport(session=session)
            return Client(url, transport=transport)


class TransmissaoHTTP(Transmissao):

    def post(self):
        pass

