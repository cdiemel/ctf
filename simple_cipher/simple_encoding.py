__author__ = 'C. Diemel'
__version__ = '1.0.0'
__name__ = 'simple_encoding.py'
__license__ = 'GPL2'
__description__ = 'Simple encoding include for simple_cipher.'

import base64
import binascii


class SimpleEncoding:
    
    _decryptions = []
    _verbosity = 0
    
    def __init__(self, logger):
        self.logger = logger
        pass
    
    def set_verbosity(self, verbosity):
        self._verbosity = verbosity
        pass
    
    def decrypt(self, cipher):
        self.base64(cipher)
        self.hex(cipher)
        self.binary(cipher)
            
        pass
    
    def base64(self, cipher):
        print("~base64~")
        b64_key = 0
        try:
            b64_decrypt = str(base64.b64decode(cipher),"utf-8")
            self._decryptions.append((b64_key,b64_decrypt))
            if self._verbosity > 2:
                print("%s: %s" %((b64_key+1),b64_decrypt))
            self.logger.info("%s: %s" %(b64_key,b64_decrypt))
        except BaseException:
            print("**Not base64\n")
        
        pass
    
    def hex(self, cipher):
        print("~hex~")
        hex_key = 0
        try:
            hex_decrypt = str(binascii.unhexlify(cipher[2:]),"utf-8")
            self._decryptions.append((hex_key,hex_decrypt))
            if self._verbosity > 2:
                print("%s: %s" %((hex_key+1),hex_decrypt))
            self.logger.info("%s: %s" %(hex_key,hex_decrypt))
        except BaseException:
            print("**Not hex\n")
        
        pass
    
    def binary(self, cipher):
        print("~binary~")
        binary_key = 0
        try:
            cipher_2 = cipher.replace(' ','')
            binary_decrypt = str(binascii.unhexlify('%x' % int(cipher_2,2)),"utf-8")
            self._decryptions.append((binary_key,binary_decrypt))
            if self._verbosity > 2:
                print("%s: %s" %((binary_key+1),binary_decrypt))
            self.logger.info("%s: %s" %(binary_key,binary_decrypt))
        except BaseException:
            print("**Not binary\n")
        
        pass
    
    def encrypt(self):
        pass
    
    