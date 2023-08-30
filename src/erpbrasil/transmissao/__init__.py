__version__ = '1.1.0'

import logging

from erpbrasil.transmissao.transmissao import TransmissaoSOAP  # noqa: F401

logging.getLogger('erpbrasil.transmissao').addHandler(logging.NullHandler())
