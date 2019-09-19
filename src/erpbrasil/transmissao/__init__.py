__version__ = '0.0.0'

import logging

logging.getLogger('erpbrasil.transmissao').addHandler(logging.NullHandler())

from .transmissao import TransmissaoSOAP
