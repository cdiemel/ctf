import simple_cipher
import sys

#cipher = "F daFJeefn  n LB-eheadty.AA1lta oiwyGW18 r a-8"
cipher = "iveghny ynxr"
if len(sys.argv) == 2:
    cipher = sys.argv[1]
simp_ciph = simple_cipher.simple_cipher(cipher)
simp_ciph.decrypt()

