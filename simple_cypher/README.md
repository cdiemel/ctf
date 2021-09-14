# Simple Cipher

## Description
Python based deciphering tool for National Cyber League competition. 

After running through all permutations, checks each permutation against english dictionary for words 3 characters or larger. Then calculates percentage of characters that are words and provides estimation of "correctness" of decipherment. 

Ciphers
- Caesar Cipher 
    - Iterates through all 26 permutations
- Atbash
    - Single attempt at reversed alphabet deciphering
- Railfence
    - Iterates through all len(cipher)/2 +1 permutations

Encoding

- base64 to ASCII
- hex to ASCII
- binary to ASCII


## Usage
#### base64

    # base64 'This is a message'
    $ python3 test_inc.py "VGhpcyBpcyBhIG1lc3NhZ2U="
Output

    ### Beginning Simple_Cipher
    
    ...

    ### Results ###
    NONE

    Encoding
    ~base64~
    1: This is a message
    
    ~hex~
    **Not hex

    ~binary~
    **Not binary

    ### Results ###
    This is a message
    78.57% - 2 - ('This', 'message')

#### Caesar Cipher

    # Caesar Cipher (5) 'This is a message'
    $ python3 test_inc.py "ymnx nx f rjxxflj"
Output

    ### Beginning Simple_Cipher

    Caesar
    1: YMNX NX F RJXXFLJ
    2: XLMW MW E QIWWEKI
    3: WKLV LV D PHVVDJH
    4: VJKU KU C OGUUCIG
    5: UIJT JT B NFTTBHF
    6: THIS IS A MESSAGE
    7: SGHR HR Z LDRRZFD
    8: RFGQ GQ Y KCQQYEC
    9: QEFP FP X JBPPXDB
    10: PDEO EO W IAOOWCA
    11: OCDN DN V HZNNVBZ
    12: NBCM CM U GYMMUAY
    13: MABL BL T FXLLTZX
    14: LZAK AK S EWKKSYW
    15: KYZJ ZJ R DVJJRXV
    16: JXYI YI Q CUIIQWU
    17: IWXH XH P BTHHPVT
    18: HVWG WG O ASGGOUS
    19: GUVF VF N ZRFFNTR
    20: FTUE UE M YQEEMSQ
    21: ESTD TD L XPDDLRP
    22: DRSC SC K WOCCKQO
    23: CQRB RB J VNBBJPN
    24: BPQA QA I UMAAIOM
    25: AOPZ PZ H TLZZHNL
    26: ZNOY OY G SKYYGMK

    ### Results ###
    THIS IS A MESSAGE
    78.57% - 2 - ('THIS', 'MESSAGE')
    
    ...

## Installation
You should just be able to clone and run as long at pycipher is installed. 
#### Requirements
- Python 3
- [pycipher](https://pypi.org/project/pycipher/)
- others? Raise an issue if you find other dependencies that were missed.

## Project status
I am currently working on this project intermitently as needed to improve my design.  Eventually I am hoping include a full menu system with colored markup.

## Support
No support is being offered at this time.  The project works for me however, YMMV.

## Contributing
No contributions being accepted at this time.  

However, feel free to clone and improve. =)

## License
For open source projects, say how it is licensed.


