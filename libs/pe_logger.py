import sys
import logging

from libs.widgets.pe_console import QtHandler

logger = logging.getLogger('prodex-desktop')
formats = '[%(levelname)s] [%(asctime)s] %(module)s.%(funcName)s | %(message)s'
formatter = logging.Formatter(formats, datefmt='%m/%d/%Y at %I:%M:%S %p')

handler = QtHandler()
handler_stream = logging.StreamHandler()
handler.setFormatter(formatter)
handler_stream.setFormatter(formatter)

logger.addHandler(handler)
logger.addHandler(handler_stream)
logger.setLevel(logging.DEBUG)