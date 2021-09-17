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



###########################
###########################
### Max Min Prompt Class
class Cypher_Prompt(Cmd):
    prompt = "\U0001F63C > "
    
    
    def do_decode(self,args):
        simp_ciph = simple_cypher.simple_cypher(args,4)
        simp_ciph.decrypt()
    
    def do_decode_external(self,args):
        cipher = "iveghny ynxr"
        verbosity = 2
        os.system('xfce4-terminal -H -x python3 simple_cypher.py {:s} "{:s}"'.format(" -v"*verbosity,cipher))
        # os.system('xfce4-terminal -H -x python3 {:s}/simple_cypher.py -v -v -v -v "iveghny ynxr"'.format(os.getcwd())
        
    ## Catch all
    def default(self, args):
        print("Bad command: %s" %args)
        
    def do_exit(self, args):
        ## Clear screen
        print('\x1bc')
        print("Exiting...")
        exit()
    
    def do_bye(self, args):
        self.do_exit(args)
        return False
        
        
cp = Cypher_Prompt()
cp.cmdloop()




# xfce-terminal -x nohup {cmd}
# choose pop up external terminal
# - xterm
# - terminator
# - xfce4-terminal
# xfce4-terminal -H -x nmap -sn 192.168.1.1