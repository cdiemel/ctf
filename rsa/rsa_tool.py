#!/usr/bin/python3
__author__ = 'C. Diemel'
__version__ = '1.0.0'
__name__ = 'rsa_tool.py'
__license__ = 'GPL2'
__description__ = 'Script to attempt to encode/decode RSA.'

import argparse

parser = argparse.ArgumentParser(prog=__file__,
                                 description="Process some integers.",
                                 epilog="RSA by C. Diemel\n")
# parser.add_argument('-p', metavar='', help='smaller prime of N')
# parser.add_argument('-q', metavar='', help='larger prime of N')
parser.add_argument('-n', metavar='', help='n: ?', type=int, required=True)
parser.add_argument('-e', metavar='', help='e: ?', type=int, required=True)
parser.add_argument('-c', metavar='', help='Cipher text to be decrypted', type=str, required=True)
args = parser.parse_args()

print(vars(args))


import math
# import sys
def extended_euclidean_algorithm(a, b):
    """
    Returns a three-tuple (gcd, x, y) such that
    a * x + b * y == gcd, where gcd is the greatest
    common divisor of a and b.

    This function implements the extended Euclidean
    algorithm and runs in O(log b) in the worst case.
    """
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t


def inverse_of(n, p):
    """
    Returns the multiplicative inverse of
    n modulo p.

    This function returns an integer m such that
    (n * m) % p == 1.
    """
    gcd, x, y = extended_euclidean_algorithm(n, p)
    assert (n * x + p * y) % p == gcd

    if gcd != 1:
        # Either n is 0, or p is not a prime number.
        raise ValueError(
            '{} has no multiplicative inverse '
            'modulo {}'.format(n, p))
    else:
        return x % p
    

def primeFactors(n): 
    n = int(n)
    while n % 2 == 0: 
        n = n / 2
        print("even: 2"), 
          
    for i in range(3,int(math.sqrt(n))+1,2): 
        while n % i== 0:  
            n = n / i
            p = i
            print("   p: %i" %p),
              
    if n > 2: 
        q = n
        print("   q: %i" %q)
    
    phi = (p-1)*(q-1)
    return p, q, phi


# i = 0
# p,q,n,e = 0,0,0,0
# cipher = []
# while i < len(sys.argv):
#     increment = 1
#     if sys.argv[i][0] == '-':
#         if sys.argv[i][1] == 'p':
#             p = int(sys.argv[i+1])
#             increment=increment+1
#         if sys.argv[i][1] == 'q':
#             q = int(sys.argv[i+1])
#             increment=increment+1
#         if sys.argv[i][1] == 'n':
#             n = int(sys.argv[i+1])
#             increment=increment+1
#         if sys.argv[i][1] == 'e':
#             e = int(sys.argv[i+1])
#             increment=increment+1
#         if sys.argv[i][1] == 'c':
#             cipher = sys.argv[i+1].split(" ")
#             increment=increment+1
#     i = i+increment

# p       = args.p
# q       = args.p
n       = args.n
e       = args.e
cipher  = args.c.split(" ")
    
if n and e and cipher:
    p, q, phi = primeFactors(n)
    d = inverse_of(e,phi)
    # c = int(c)
    d = int(d)
    n = int(n)
print("p=%i" %p)
print("q=%i" %q)
print("n=%i" %n)
print("d=%i" %d)
print("e=%i" %e)
print("c=%s" %cipher)

msg = ''
msg2 = ''
for c in cipher:
    print(c)
    msg = msg + chr(pow(int(c),d,n))
    msg2 = ("%s %s" %(msg2,pow(int(c),d,n)))

print(("D %s" %msg))
print(("E %s" %msg2))

## Decrypt
## python3 rsa_test.py -n 1829 -e 791 -c '668 516 229 668 542 516 229 229 881 1378 516'
## Encrypt
## python3 rsa_test.py -n 1829 -e 11 -c '84 69 83 84 77 69 83 83 65 71 69'
