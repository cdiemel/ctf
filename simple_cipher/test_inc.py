import simple_cipher
import sys
import argparse

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
print(args)
print(args.verbose)
print(args.cipher)

simp_ciph = simple_cipher.simple_cipher(args.cipher,args.verbose)
simp_ciph.decrypt()