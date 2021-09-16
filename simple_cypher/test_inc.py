import simple_cypher
import sys
import argparse
from cmd import Cmd

#cipher = "F daFJeefn  n LB-eheadty.AA1lta oiwyGW18 r a-8"
# cipher = "iveghny ynxr"
# if len(sys.argv) == 2:
#     cipher = sys.argv[1]
# simp_ciph = simple_cipher.simple_cipher(cipher)
# simp_ciph.decrypt()



parser = argparse.ArgumentParser()
parser.add_argument('--verbose', '-v', action='count', default=0, help="Set verbosity level")
parser.add_argument("cipher", help="Cipher to be decoded")

args = parser.parse_args()
# print(args)
# print(args.verbose)
# print(args.cipher)

simp_ciph = simple_cypher.simple_cypher(args.cipher,args.verbose)
simp_ciph.decrypt()

###########################
###########################
### Max Min Prompt Class
class Cypher_Prompt(Cmd):
    prompt = "\U0001F63C > "
    
    
    def do_decode(self,args):
        simp_ciph = simple_cypher.simple_cypher(args,4)
        simp_ciph.decrypt()
        
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
        
        
# cp = Cypher_Prompt()
# cp.cmdloop()




# xfce-terminal -x nohup {cmd}
# choose pop up external terminal
# - xterm
# - terminator
# - xfce-terminal
# xfce4-terminal -H -x nmap -sn 192.168.1.1