#!/usr/bin/python3

__author__ = 'C. Diemel'
__version__ = '2.4.0'
__name__ = 'simple_cypher.py'
__license__ = 'GPL2'
__description__ = 'Script to attempt to decode simple text ciphers. Caesar, RailFence, etc.'


import os
import re
import sys
import time
import logging
import argparse
import pyperclip
from datetime import datetime
from simple_caesar import SimpleCaesar
from simple_vigenere import SimpleVigenere
from simple_railfence import SimpleRailFence
from simple_atbash import SimpleAtbash
from simple_encoding import SimpleEncoding
from simple_morse import SimpleMorse

## TODO:  Add dictionary support

class simple_cypher:
    
    logger      = None
    _cipher     = ''
    # _caesar     = []
    _railfence  = []
    _prob       = {}
    _c_classes  = {}
    _verbosity  = 0
    
    def __init__(self, cipher, key, verbosity=0):
        self._verbosity = verbosity
        self._set_cipher(cipher)
        self._setup_logger()
        self._setup_dictionary()
        self._add_cipher(SimpleCaesar, 'Caesar', 0)
        self._add_cipher(SimpleRailFence, 'RailFence', 0)
        self._add_cipher(SimpleAtbash, 'Atbash', 0)
        self._add_cipher(SimpleEncoding, 'Encoding', 0)
        self._add_cipher(SimpleMorse, 'Morse Code', 0)
        if key:
            self._set_key(key)
            self._add_cipher(SimpleVigenere, 'Vigenere', 1)
        return
    
    def _add_cipher(self, cipher, label, key_bool):
        # self._c_classes[lable] = {'class':cipher, 'decrypt':None, 'dict':None}
        self._c_classes[label] = {'class':cipher, 'has_key':key_bool, 'dict':None}
        return
    
    def decrypt(self):
        # print(self._c_classes)
        self.logger.info("### Beginning Simple_Cipher")
        # -v +
        if self._verbosity > 0:
            print("### Beginning Simple_Cipher")
        for name in self._c_classes:
            # -v +
            if self._verbosity > 0:
                print("\n" + name)
            cipher = self._c_classes[name]
            c_class = cipher['class'](self.logger)
            # print(c_class)
            c_class.set_verbosity(self._verbosity)
            if cipher['has_key']:
                c_class.decrypt(self._cipher,self._key)
            else:
                c_class.decrypt(self._cipher)
        
            # print(c_class._decryptions)
            self._check_dictionary(c_class._decryptions)
        if self._verbosity < 4:
            self._print_probability(self._prob)
            
    def _set_cipher(self, ciph):
        self._cipher = ciph
        
    def _set_key(self, key):
        self._key = key
    
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
    
    def _check_dictionary(self, *args):
        if self._verbosity > 3:
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
        if self._verbosity > 3:
            self._print_probability(self._prob)
    
    def _print_probability(self, tmpset):
        green = u'\u001b[32m'
        yellow = u'\u001b[33m'
        red = u'\u001b[31m'
        reset = u'\u001b[0m'

        print("\n### Results ###")
        self.logger.info("\n### Results ###")
        
        if len(tmpset) == 0:
            print("NONE")
            self.logger.info(" ** NONE **")
            return
        
        cur_max_percent = 0
        #cur_max_key = ""
        
        for key in tmpset:
            color = red
            if tmpset[key]["percent"] > 65:
                color = green
            elif tmpset[key]["percent"] > 30:
                color = yellow
            print(color+key+reset)
            
            if tmpset[key]["percent"] > cur_max_percent:
                cur_max_percent = tmpset[key]["percent"]
                #cur_max_key = key
                
            print("%s %s%% - %s - %s %s" %(color,tmpset[key]["percent"],tmpset[key]["count"],tmpset[key]["words"],reset))
            graph_char_count = round(tmpset[key]["percent"]/5)
            graph_chars = "#"*graph_char_count
            r = graph_chars[0:6]
            y = graph_chars[6:12]
            g = graph_chars[12:20]
            print("[{}{:6s}{}{:6s}{}{:8s}{}]{}%".format(red,r,yellow,y,green,g,reset,tmpset[key]["percent"]))
            
            self.logger.critical("  %s%% - %s - %s\nRotation: %s\n%s\n" %(tmpset[key]["percent"],tmpset[key]["count"],tmpset[key]["words"],tmpset[key]["rotation"],key))
            # self.logger.info("%s  -  %s" %(tmpset[key],key))

        pyperclip.copy(key)
        time.sleep(1)


# Parse cli arguments
parser = argparse.ArgumentParser()
parser.add_argument('--verbose', '-v', action='count', default=0, help="Set verbosity level")
parser.add_argument('--key', '-k', action='store', help="Decipher key")
p_group = parser.add_mutually_exclusive_group(required=True)
p_group.add_argument('--clipboard', '-c', action='store_const', default=0, const=1, help="Copy from/to clipboard")
p_group.add_argument("cipher", nargs='?', help="Cipher to be decoded")

args = parser.parse_args()

## copy from clipboard
if args.clipboard:
    args.cipher = pyperclip.paste()

print(args)

simp_ciph = simple_cypher(args.cipher,args.key,args.verbose)
simp_ciph.decrypt()


