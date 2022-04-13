__author__ = 'C. Diemel'
__version__ = '1.3.0'
__name__ = 'simple_railfence.py'
__license__ = 'GPL2'
__description__ = 'RailFence include for simple_cipher.'

import sys
from math import ceil
from pycipher import Railfence

## this checks to see if we
## calling the file directly
if sys.argv[0] == __name__:
    exit()

class SimpleRailFence:
    
    _decryptions = []
    _verbosity = 0
    
    def __init__(self, logger):
        self.logger = logger
    
    def set_verbosity(self, verbosity):
        self._verbosity = verbosity
    
    def decrypt(self, cipher):
        self.logger.info("### RailFence Cipher ###")
        for rf_key in range(2,ceil(len(cipher)/2)+1,1):
            rf_decrypt = Railfence(rf_key).decipher(cipher,True)
            self._decryptions.append((rf_key,rf_decrypt))
            # -v -v +
            if self._verbosity > 2:
                print("%s: %s" %((rf_key-1),rf_decrypt))
            self.logger.info("%s: %s" %(rf_key,rf_decrypt))
    
    def encrypt(self):
        pass
    
    