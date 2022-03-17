#!/usr/bin/python3
__author__ = 'C. Diemel'
__version__ = '1.0.0'
__name__ = 'simple_morse.py'
__license__ = 'GPL2'
__description__ = 'Script to attempt to decode morse code.'

import sys

## this checks to see if we
## calling the file directly
if sys.argv[0] == __name__:
    exit()


# letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','o','n','p','q','r','s','t','u','v','w','x','y','z']
# numbers=['0','1','2','3','4','5','6','7','8','9']
# special=['!','@','$','&','(',')','_','-','+','=',';',"'",':','"',',','.','/','?']
# morse_special=['-.-.--','.--.-.','...-..-','.-...','-.--.','-.--.-','..--.-','-....-','.-.-.','-...-','-.-.-','.----.','---...','.-..-.','--..--','.-.-.-','-..-.','..--..']
# morse_letters=['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','---','-.','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']
# morse_numbers=['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','---','-.','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']
class SimpleMorse:
    
    _decryptions = []
    _verbosity = 0
    
    let2morse_dict = {
        'a': '.-',
        'b': '-...',
        'c': '-.-.',
        'd': '-..',
        'e': '.',
        'f': '..-.',
        'g': '--.',
        'h': '....',
        'i': '..',
        'j': '.---',
        'k': '-.-',
        'l': '.-..',
        'm': '--',
        'o': '---',
        'n': '-.',
        'p': '.--.',
        'q': '--.-',
        'r': '.-.',
        's': '...',
        't': '-',
        'u': '..-',
        'v': '...-',
        'w': '.--',
        'x': '-..-',
        'y': '-.--',
        'z': '--..'
    }
    
    morse2let_dict = {
        '.-': 'a',
        '-...': 'b',
        '-.-.': 'c',
        '-..': 'd',
        '.': 'e',
        '..-.': 'f',
        '--.': 'g',
        '....': 'h',
        '..': 'i',
        '.---': 'j',
        '-.-': 'k',
        '.-..': 'l',
        '--': 'm',
        '---': 'o',
        '-.': 'n',
        '.--.': 'p',
        '--.-': 'q',
        '.-.': 'r',
        '...': 's',
        '-': 't',
        '..-': 'u',
        '...-': 'v',
        '.--': 'w',
        '-..-': 'x',
        '-.--': 'y',
        '--..': 'z'
    }
    
    num2morse_dict = {
        '0': '.-',
        '1': '-...',
        '2': '-.-.',
        '3': '-..',
        '4': '.',
        '5': '..-.',
        '6': '--.',
        '7': '....',
        '8': '..',
        '9': '.---'
    }
    
    morse2num_dict = {
        '.-': '0',
        '-...': '1',
        '-.-.': '2',
        '-..': '3',
        '.': '4',
        '..-.': '5',
        '--.': '6',
        '....': '7',
        '..': '8',
        '.---': '9'
    }
    
    spec2morse_dict = {}
    
    morse2spec_dict = {
        '-.-.--': '!',
        '.--.-.': '@',
        '...-..-': '$',
        '.-...': '&',
        '-.--.': '(',
        '-.--.-': ')',
        '..--.-': '_',
        '-....-': '-',
        '.-.-.': '+',
        '-...-': '=',
        '-.-.-': ';',
        '.----.': "'",
        '---...': ':',
        '.-..-.': '"',
        '--..--': ',',
        '.-.-.-': '.',
        '-..-.': '/',
        '..--..': '?'
    }

    def __init__(self, logger):
        self.logger = logger
        pass
    
    def set_verbosity(self, verbosity):
        self._verbosity = verbosity
        pass 
    
    def decrypt(self, cipher):
        morse_words = cipher.split("/")
        morse_decrypt = ""
        morse_key = 0
        for w in morse_words:
            # w = w.strip()
            for l in w.strip().split(" "):
                if l in self.morse2let_dict:
                    morse_decrypt += self.morse2let_dict[l]
                elif l in self.morse2num_dict:
                    morse_decrypt += self.morse2num_dict[l]
                elif l in self.morse2spec_dict:
                    morse_decrypt += self.morse2spec_dict[l]
                
            morse_decrypt += " "
        
        self._decryptions.append((morse_key,morse_decrypt))
        if self._verbosity > 2:
            print("%s: %s" %((morse_key+1),morse_decrypt))
        self.logger.info("%s: %s" %(morse_key,morse_decrypt))
    
    def encrypt(self):
        pass    
    
    
#     
# for i in range(len(special)):
#     print("'{}': '{}',".format(morse_special[i],special[i]))
#     
#     
    