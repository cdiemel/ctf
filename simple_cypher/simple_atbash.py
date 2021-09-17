__author__ = 'C. Diemel'
__version__ = '1.0.0'
__name__ = 'simple_atbash.py'
__license__ = 'GPL2'
__description__ = 'Atbash Cipher include for simple_cipher.'

import sys
from pycipher import Atbash

## this checks to see if we
## calling the file directly
if sys.argv[0] == __name__:
    exit()
    
class SimpleAtbash:
    
    _decryptions = []
    _verbosity = 0
    
    def __init__(self, logger):
        self.logger = logger
        pass
    
    def set_verbosity(self, verbosity):
        self._verbosity = verbosity
        pass 
    
    def decrypt(self, cipher):
        a_key = 0
        a_decrypt = Atbash().decipher(cipher,True)
        self._decryptions.append((a_key,a_decrypt))
        # -v -v +
        if self._verbosity > 2:
                print("%s: %s" %((a_key+1),a_decrypt))
        self.logger.info("%s: %s" %(a_key,a_decrypt))
            
        pass
    
    def encrypt(self):
        pass
    
    