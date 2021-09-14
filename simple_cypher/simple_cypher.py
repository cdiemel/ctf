#!/usr/bin/python3
__author__ = 'C. Diemel'
__version__ = '1.3.0'
__name__ = 'simple_cipher.py'
__license__ = 'GPL2'
__description__ = 'Script to attempt to decode simple text ciphers. Caesar, RailFence, etc.'


import sys
import re
import logging
import time
import os
from datetime import datetime
# from pycipher import Caesar
# from pycipher import Railfence
from simple_caesar import SimpleCaesar
from simple_railfence import SimpleRailFence
from simple_atbash import SimpleAtbash
from simple_encoding import SimpleEncoding

## TODO:  Add dictionary support

class simple_cypher:
    
    logger      = None
    _cipher     = ''
    # _caesar     = []
    _railfence  = []
    _prob       = {}
    _c_classes  = {}
    _verbosity  = 0
    
    def __init__(self, cipher, verbosity=0):
        self._verbosity = verbosity
        self._set_cipher(cipher)
        self._setup_logger()
        self._setup_dictionary()
        self._add_cipher(SimpleCaesar, 'Caesar')
        self._add_cipher(SimpleRailFence, 'RailFence')
        self._add_cipher(SimpleAtbash, 'Atbash')
        self._add_cipher(SimpleEncoding, 'Encoding')
        return
    
    def _add_cipher(self, cipher, label):
        # self._c_classes[lable] = {'class':cipher, 'decrypt':None, 'dict':None}
        self._c_classes[label] = {'class':cipher, 'dict':None}
        return
    
    def decrypt(self):
        # print(self._c_classes)
        self.logger.info("### Beginning Simple_Cipher")
        print("### Beginning Simple_Cipher")
        for name in self._c_classes:
            print("\n" + name)
            cipher = self._c_classes[name]
            c_class = cipher['class'](self.logger)
            # print(c_class)
            c_class.set_verbosity(self._verbosity)
            c_class.decrypt(self._cipher)
        
            # print(c_class._decryptions)
            self._check_dictionary(c_class._decryptions)
            
    def _set_cipher(self, ciph):
        self._cipher = ciph
    
    def get_cipher(self):
        return self._cipher
    
    def get_logger(self):
        return self.logger
        
    def _setup_logger(self):
        # if ! logs folder, create one
        None if os.path.isdir('logs') else os.mkdir('logs')

        dateTimeObj = datetime.now()
        timestampStr = dateTimeObj.strftime("%Y%m%d.%H%M.%S")
        logging.basicConfig(filename="logs/simple_cipher."+timestampStr+".log", filemode='a', format='%(levelname)s:%(message)s', level=logging.INFO)
        self.logger = logging.getLogger("simple_cipher")
        self.logger.info("Arguments:\n\n"+str(sys.argv)+"\n")
        return self.logger
    
    def _setup_dictionary(self, filename=None):
        if not filename:
            filename = "/usr/share/dict/american-english"
        self._dictionary = set(str.lower(line.strip()) for line in open(filename))
        pass
    
    def _check_dictionary(self, *args):
        self._prob = {}
        for ptext in args[0]:
            decrypted_text = ptext[1]
            for word in re.split('(\W+)',decrypted_text):
                if len(word) > 2 and str.lower(word) in self._dictionary:
                    # print(word)
                    if decrypted_text not in self._prob:
                        self._prob[decrypted_text] = {"count":0,"percent":0,"words":(),"rotation":ptext[0]}
                    
                    self._prob[decrypted_text]["count"]   = self._prob[decrypted_text]["count"] + 1
                    self._prob[decrypted_text]["percent"] = round(self._prob[decrypted_text]["percent"] + (len(word)/len(decrypted_text.replace(" ", ""))*100),2)
                    self._prob[decrypted_text]["words"]   = self._prob[decrypted_text]["words"] + (word,)
        
        self._print_probability(self._prob)
    
    def _print_probability(self, tmpset):
        
        print("\n### Results ###")
        self.logger.info("\n### Results ###")
        
        if len(tmpset) == 0:
            print("NONE")
            self.logger.info(" ** NONE **")
            return
        
        for key in tmpset:
            print(key)
            print("%s%% - %s - %s\n" %(tmpset[key]["percent"],tmpset[key]["count"],tmpset[key]["words"]))
            self.logger.critical("  %s%% - %s - %s\nRotation: %s\n%s\n" %(tmpset[key]["percent"],tmpset[key]["count"],tmpset[key]["words"],tmpset[key]["rotation"],key))
            # self.logger.info("%s  -  %s" %(tmpset[key],key))

## This next section makes the script
## both runnable and able to be included

def not_included(cipher):
    simp_ciph = simple_cypher(cipher)
    simp_ciph.decrypt()

## this checks to see if we
## calling the file directly
if sys.argv[0] == __name__ and len(sys.argv) == 2:
    print("not included")
    not_included(sys.argv[1])
