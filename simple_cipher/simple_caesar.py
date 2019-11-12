

from pycipher import Caesar


class SimpleCaesar:
    
    _decryptions = []
    
    def __init__(self, logger):
        self.logger = logger
        pass
    
    def decrypt(self, cipher):
        for c_key in range(1,26,1):
            c_decrypt = Caesar(c_key).decipher(cipher,True)
            self._decryptions.append((c_key,c_decrypt))
            print("%s: %s" %(c_key,c_decrypt))
            self.logger.info("%s: %s" %(c_key,c_decrypt))
            
        pass
    
    def encrypt(self):
        pass
    
    