__author__ = 'C. Diemel'
__version__ = '1.3.0'
__name__ = 'simple_vigenere.py'
__license__ = 'GPL2'
__description__ = 'Vigenere Cipher include for simple_cipher.'

import re
import sys
import math
from pycipher import Vigenere

## this checks to see if we
## calling the file directly
if sys.argv[0] == __name__:
    exit()

class SimpleVigenere:
    
    _decryptions = []
    _verbosity = 0
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    def __init__(self, logger):
        self.logger = logger
        pass
    
    def set_verbosity(self, verbosity):
        self._verbosity = verbosity
        pass 
    
    def decrypt(self, cipher, key):
        vigenere_key = 0
        self.full_key = key*(math.ceil(len(cipher)/len(key)))
        v_decrypt = ""
        v_txt_offset = 0
        
        for i in range(len(cipher)):
            c_char = cipher[i]
            
            if self.alph.upper().find(c_char) > -1:
                k = self.full_key[i-v_txt_offset].upper()
                v_decrypt += self.decode_char(self.alph.upper(),c_char,k)
            elif self.alph.lower().find(c_char) > -1:
                k = self.full_key[i-v_txt_offset].lower()
                v_decrypt += self.decode_char(self.alph.lower(),c_char,k)
            else:
                v_decrypt += c_char
                v_txt_offset += 1
            
        self._decryptions.append((vigenere_key,v_decrypt))
        if self._verbosity > 2:
            print("%s: %s" %((vigenere_key+1),v_decrypt))
        self.logger.info("%s: %s" %(vigenere_key,v_decrypt))
            
        pass
    
    def decode_char(self,charset,cipher_char,key_char):
        k_index     = charset.find(key_char)
        tmp_charset = charset[k_index:]+charset[:k_index]
        c_index     = tmp_charset.find(cipher_char)
        return charset[c_index]
    
    def encrypt(self):
        pass
    
    