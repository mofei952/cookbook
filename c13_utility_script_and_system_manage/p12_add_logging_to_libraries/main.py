import logging
import somelib


logging.basicConfig()
somelib.func()
print()

logging.getLogger('somelib').level = logging.DEBUG
somelib.func()
logging.debug('111')
logging.warning('111')
