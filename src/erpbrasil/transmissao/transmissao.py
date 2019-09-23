# coding=utf-8
# Copyright (C) 2019  Luis Felipe Mileo - KMEE

import os
import abc
import tempfile

from erpbrasil.assinatura.certificado import ArquivoCertificado
from erpbrasil.assinatura.certificado import Certificado
from requests import Session
from zeep import Client
from requests.auth import HTTPBasicAuth
from zeep.transports import Transport
from zeep.cache import SqliteCache

ABC = abc.ABCMeta('ABC', (object,), {})


class Transmissao(ABC):
    """
    Classe abstrata responsavel por definir os metodos e logica das classes
    de transmissao com os webservices.
    """

    @abc.abstractmethod
    def post(self):
        pass

    @abc.abstractmethod
    def cliente(self):
        pass


class TransmissaoSOAP(Transmissao):

    def __init__(self, certificado, cache=True):
        """
        :param certificado: erpbrasil.assinatura.certificado
        :param cache: O cache torna as requisições mais rápidas entretanto,
        pode causar problemas em caso de troca de parametros dos webservices
        """
        if cache:
            self._cache = self.get_cache()
        self.certificado = certificado

    def post(self):
        pass

    def cliente(self, url, verify=False):
        with ArquivoCertificado(self.certificado, 'w') as (key, cert):
            session = Session()
            session.cert = (key, cert)
            session.verify = verify

            transport = Transport(session=session, cache=self.cache)
            return Client(url, transport=transport)

    @staticmethod
    def get_cache():
        temp_dir = tempfile.gettempdir()
        cache_file = os.path.join(temp_dir, 'erpbrasil_transmissao.db')
        return SqliteCache(path=cache_file, timeout=60)

class TransmissaoHTTP(Transmissao):

    def post(self):
        pass

    def cliente(self, url, user, password, auth=HTTPBasicAuth):
        session = Session()
        session.auth = auth(user, password)
        return Client(url, transport=Transport(session=session))
