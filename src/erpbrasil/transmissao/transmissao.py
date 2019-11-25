# coding=utf-8
# Copyright (C) 2019  Luis Felipe Mileo - KMEE

import abc
import os
import tempfile
from contextlib import contextmanager

import requests
from erpbrasil.assinatura.certificado import ArquivoCertificado
from lxml import etree
from requests import Session
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from zeep import Client
from zeep.cache import SqliteCache
from zeep.transports import Transport

ABC = abc.ABCMeta('ABC', (object,), {})


class Transmissao(ABC):
    """
    Classe abstrata responsavel por definir os metodos e logica das classes
    de transmissao com os webservices.
    """

    @abc.abstractmethod
    def enviar(self):
        pass

    @abc.abstractmethod
    def cliente(self):
        pass


class TransmissaoSOAP(Transmissao):

    def __init__(self, certificado, session=Session(), cache=True,
                 disable_warnings=True, raw_response=True):
        """
        :param certificado: erpbrasil.assinatura.certificado
        :param cache: O cache torna as requisições mais rápidas entretanto,
        pode causar problemas em caso de troca de parametros dos webservices
        """
        if cache:
            self._cache = self.get_cache()
        self.certificado = certificado
        self.session = session
        self._disable_warnings = disable_warnings
        self.raw_response = raw_response

    @staticmethod
    def get_cache():
        temp_dir = tempfile.gettempdir()
        cache_file = os.path.join(temp_dir, 'erpbrasil_transmissao.db')
        return SqliteCache(path=cache_file, timeout=60)

    def desativar_avisos(self):
        if self._disable_warnings:
            requests.packages.urllib3.disable_warnings(
                InsecureRequestWarning
            )

    @contextmanager
    def cliente(self, url, verify=False, service_name=None, port_name=None):
        with ArquivoCertificado(self.certificado, 'w') as (key, cert):
            self.desativar_avisos()
            session = Session()
            session.cert = (key, cert)
            session.verify = verify
            transport = Transport(session=session, cache=self._cache)
            self._cliente = Client(
                url, transport=transport, service_name=service_name,
                port_name=port_name
            )
            yield self._cliente
            self._cliente = False

    def interpretar_mensagem(self, mensagem):
        if type(mensagem) == str:
            return etree.fromstring(mensagem, parser=etree.XMLParser(
                remove_blank_text=True
            ))
        return mensagem

    def set_header(self, elemento, **kwargs):
        header_element = self._cliente.get_element(elemento)
        header = header_element(**kwargs)
        self._cliente.set_default_soapheaders([header])

    def enviar(self, operacao, mensagem):
        with self._cliente.settings(raw_response=self.raw_response):
            return self._cliente.service[operacao](
                self.interpretar_mensagem(mensagem)
            )


class TransmissaoHTTP(Transmissao):

    def enviar(self):
        pass

    def cliente(self, url, user, password, auth=HTTPBasicAuth):
        session = Session()
        session.auth = auth(user, password)
        return Client(url, transport=Transport(session=session))
