#!/usr/bin/python3
# _author_ C. Diemel


import sys
import re
import logging
import time
# from pycipher import Caesar
# from pycipher import Railfence
from simple_caesar import SimpleCaesar
from simple_railfence import SimpleRailFence

## TODO:  Add dictionary support

class simple_cipher:
    
    logger      = None
    _cipher     = ''
    # _caesar     = []
    _railfence  = []
    _prob       = {}
    _c_classes  = {}
    
    def __init__(self, cipher):
        self._set_cipher(cipher)
        self._setup_logger()
        self._setup_dictionary()
        self._add_cipher(SimpleCaesar, 'Caesar')
        self._add_cipher(SimpleRailFence, 'RailFence')
        return
    
    def _add_cipher(self, cipher, lable):
        # self._c_classes[lable] = {'class':cipher, 'decrypt':None, 'dict':None}
        self._c_classes[lable] = {'class':cipher, 'dict':None}
        return
    
    def decrypt(self):
        print(self._c_classes)
        self.logger.info("### Beginning Simple_Cipher")
        for name in self._c_classes:
            cipher = self._c_classes[name]
            c_class = cipher['class'](self.logger)
            print(c_class)
            c_class.decrypt(self._cipher)
        
            print(c_class._decryptions)
        
        # named_tuple = time.localtime() # get struct_time
        # time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
        # self.logger.info("### %s" %time_string)
        # self.logger.info("### %s" %self._cipher)
        # 
        # self._decrypt_caesar(self._cipher)
        # self._decrypt_railfence(self._cipher)
        # self._check_dictionary(self._caesar, self._railfence)
    
    # def _decrypt_caesar(self, ciph):
    #     self.logger.info("### Caesar Cipher ###")
    #     for c_key in range(1,26,1):
    #         c_decrypt = Caesar(c_key).decipher(ciph,True)
    #         self._caesar.append(c_decrypt)
    #         print("%s: %s" %(c_key,c_decrypt))
    #         self.logger.info("%s: %s" %(c_key,c_decrypt))
    # 
    # def _decrypt_railfence(self, ciph):
    #     self.logger.info("### RailFence Cipher ###")
    #     for rf_key in range(2,ceil(len(ciph)/2)+1,1):
    #         rf_decrypt = Railfence(rf_key).decipher(ciph,True)
    #         self._railfence.append(rf_decrypt)
    #         print("%s: %s" %(rf_key,rf_decrypt))
    #         self.logger.info("%s: %s" %(rf_key,rf_decrypt))
            
    def _set_cipher(self, ciph):
        self._cipher = ciph
    
    def get_cipher(self):
        return self._cipher
    
    def get_logger(self):
        return self.logger
        
    def _setup_logger(self):
        logging.basicConfig(filename='simple_ciphers.log', filemode='a', level=logging.INFO)
        self.logger = logging.getLogger("simple_cipher")
        return self.logger
    
    def _setup_dictionary(self, filename=None):
        if not filename:
            filename = "/usr/share/dict/american-english"
        self._dictionary = set(str.lower(line.strip()) for line in open(filename))
        pass
    
    def _check_dictionary(self, *args):
        for plist in args:
            tmpset = {}
            for ptext in plist:
                for word in re.split('(\W+)',ptext):
                    if len(word) > 2 and str.lower(word) in self._dictionary:
                        print(word)
                        if ptext not in self._prob:
                            self._prob[ptext] = 0
                        
                        self._prob[ptext] = self._prob[ptext] + 1
                        
                        # if ptext not in tmpset:
                        #     tmpset[ptext] = 0
                        #     
                        # tmpset[ptext] = tempset[ptext] + 1
            
            # self._print_probability(self._prob, args[plist])
            self._print_probability(self._prob)
    
    # def _print_probability(self, tmpset, label):
    def _print_probability(self, tmpset):
        tmplist = {}
        # for key in self._prob:
        #     print("%s  -  %s" %(self._prob[key],key))
        #     self.logger.info("%s  -  %s" %(self._prob[key],key))
        for key in tmpset:
            print("%s  -  %s" %(tmpset[key],key))
            self.logger.info("%s  -  %s" %(tmpset[key],key))
        #     if self._prob[key] not in tmplist:
        #         tmplist[self._prob[key]] = [key]
        #     else:
        #         tmplist[self._prob[key]].append(key)
        #         
        # print(tmplist)


## This next section makes the script
## both runnable and able to be included

def no_run(cipher):
    simp_ciph = simple_cipher(cipher)
    simp_ciph.decrypt()

## this checks to see if we
## calling the file directly
if sys.argv[0] == __file__ and len(sys.argv) == 2:
    no_run(sys.argv[1])
    
    
# {   'caesar':{
#             'decrypt':[
#                     ('1','abc123'),
#                     ('2','acb321')],
#             'dict':[
#                     ('5','abc123'),
#                     ('1','cba321')
#                     ]
#             },
#     'railfence':{
#             'decrypt':[
#                     ('1','abc123'),
#                     ('2','acb321')
#                     ],
#             'dict':[
#                     ('5','abc123'),
#                     ('1','cba321')
#                     ]
#             }
# }
