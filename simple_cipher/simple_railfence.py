

from math import ceil
from pycipher import Railfence


class SimpleRailFence:
    
    _decryptions = []
    
    def __init__(self, logger):
        self.logger = logger
        pass
    
    def decrypt(self, cipher):
        self.logger.info("### RailFence Cipher ###")
        for rf_key in range(2,ceil(len(cipher)/2)+1,1):
            rf_decrypt = Railfence(rf_key).decipher(cipher,True)
            self._decryptions.append((rf_key,rf_decrypt))
            print("%s: %s" %(rf_key,rf_decrypt))
            self.logger.info("%s: %s" %(rf_key,rf_decrypt))
            
        pass
    
    def encrypt(self):
        pass
    
    