__author__ = 'C. Diemel'
__version__ = '2.0.0'
__name__ = 'cli.py'
__license__ = 'GPL2'
__description__ = 'CLI interface for Simple Cypher.'

import os
import sys
import simple_cypher
from cmd import Cmd

#cipher = "F daFJeefn  n LB-eheadty.AA1lta oiwyGW18 r a-8"
# cipher = "iveghny ynxr"
# if len(sys.argv) == 2:
#     cipher = sys.argv[1]
# simp_ciph = simple_cipher.simple_cipher(cipher)
# simp_ciph.decrypt()



# cipher = "iveghny ynxr"

###########################
###########################
### Max Min Prompt Class
class Cypher_Prompt(Cmd):
    prompt = "\U0001F63C > "
    _verbosity = 0
    _cipher    = ''
    _external  = 0
    
    
    def do_decode(self,args):
        'Help text'
        cipher = self._cipher
        verbosity = self._verbosity
        if self._external:
            os.system('nohup xfce4-terminal -H -x python3 simple_cypher.py {:s} "{:s}" 2>/dev/null&'
                  .format(" -v"*verbosity,cipher))
            print(self.prompt)
        else:
            simp_ciph = simple_cypher.simple_cypher(cipher,verbosity)
            simp_ciph.decrypt()
    
    # def do_decode_external(self,args):
    #     'Help text'
    #     cipher = "iveghny ynxr"
    #     verbosity = self._verbosity
    #     verbosity = 2
    #     
    #     # os.system('xfce4-terminal -H -x python3 {:s}/simple_cypher.py -v -v -v -v "iveghny ynxr"'.format(os.getcwd())
    #     
    def do_setup(self,args):
        'Help text'
        cipher = ''
        cipher = str(input('Cipher:'))
        if not cipher:
            self._cipher = ''
        else:
            self._cipher = cipher
        
        verb = 0
        try:
            verb = int(input('Verbosity[1-4][0]: '))
            if verb:
                self._verbosity = verb
        except ValueError:
            self._verbosity = 0
        
        self._external = 0
        external = str(input("Launch externally[n]: "))
        if external.lower() == 'y':
            self._external = 1
            
        print("Cipher: {}".format(self._cipher))
        print("Vebose: {}".format(self._verbosity))
        print("Extern: {}".format(self._external))
    
    def do_exit(self, args):
        'Help text'
        ## Clear screen
        print('\x1bc')
        print("Exiting...")
        exit()
    
    def do_bye(self, args):
        'Help text'
        self.do_exit(args)
        return False
    
    ## Catch all
    def default(self, args):
        print("Bad command: %s" %args)
        
    ######################
    ## PRIVATE FUNCTION ##
    ######################
    
    def set_verbosity(self,verbosity):
        self._verbosity = verbosity
    
    def set_cipher(self,cipher):
        self._cipher = cipher
        
    def emptyline(self):
         pass
        
        
cp = Cypher_Prompt()
cp.cmdloop()




# xfce-terminal -x nohup {cmd}
# choose pop up external terminal
# - xterm
# - terminator
# - xfce4-terminal
# xfce4-terminal -H -x nmap -sn 192.168.1.1