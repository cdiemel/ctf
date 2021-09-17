__author__ = 'C. Diemel'
__version__ = '1.3.0'
__name__ = 'simple_caesar.py'
__license__ = 'GPL2'
__description__ = 'Caesar Cipher include for simple_cipher.'

import sys
from pycipher import Caesar

## this checks to see if we
## calling the file directly
if sys.argv[0] == __name__:
    exit()

class SimpleCaesar:
    
    _decryptions = []
    _verbosity = 0
    
    def __init__(self, logger):
        self.logger = logger
        pass
    
    def set_verbosity(self, verbosity):
        self._verbosity = verbosity
        pass 
    
    def decrypt(self, cipher):
        for c_key in range(0,26,1):
            c_decrypt = Caesar(c_key).decipher(cipher,True)
            self._decryptions.append((c_key,c_decrypt))
            # -v -v +
            if self._verbosity > 2:
                print("%s: %s" %((c_key+1),c_decrypt))
            self.logger.info("%s: %s" %(c_key,c_decrypt))
            
        pass
    
    def encrypt(self):
        pass
    
    