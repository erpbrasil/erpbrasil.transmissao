__version__ = '0.0.0'

import logging

logging.getLogger('erpbrasil.transmissao').addHandler(logging.NullHandler())

from erpbrasil.transmissao.transmissao import TransmissaoSOAP  # noqa: F401

