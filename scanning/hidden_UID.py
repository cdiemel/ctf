#!/usr/bin/python3
__author__ = 'C. Diemel'
__version__ = '1.0.0'
__name__ = 'hidden_UID.py'
__license__ = 'GPL2'
__description__ = 'autoconnect to remote port, fuzz UID value'


import logging
# import time
import socket
# import sys
import math
import argparse

warn = ""
warn = warn+"** WARNING **\n"
warn = warn+"THIS SENDS A SIGNIFICANT AMOUNT OF TRAFFIC\n"
warn = warn+"DO NOT USE IF YOU DO NOT UNDERSTAND WHAT\n"
warn = warn+"YOU ARE DOING, YOU HAVE BEEN WARNED."

parser = argparse.ArgumentParser(prog=__file__,
                                 description="Fuzz UID.\n"+warn,
                                 epilog="UID fuzzer by C. Diemel\n")
parser.add_argument('-a', metavar='', help='IP address', type=str, required=True)
parser.add_argument('-p', metavar='', help='Port number', type=int, required=True)
args = parser.parse_args()

print(vars(args))

fn = args.a.replace('.','-')+'_'+str(args.p)+'_UID.log'
logging.basicConfig(filename=fn, filemode='w', level=logging.DEBUG)

alpha   = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num     = ['0','1','2','3','4','5','6','7','8','9']
spec    = ['-','_','=','+','\\','/','.',',','<','>','?',':','"',"'",'{','}','[',']','|',')','(','*','&','^','%',"$","#","@",'!','~','`']


def get_ans(r):
    ans = ''
    inc = r % 8
    # for i in range(0,inc+1,1):
    i = 0
    inc2 = inc * 2
    if r > 248 :
        char = '1'
        sc = math.floor(r / 8 ) % 31
        sc_val = spec[sc-1]
    else:
        char = 'a'
        sc = math.floor(r / 8)
        sc_val = spec[sc-1]
        
    while i <= inc2:
        print(i)
        i = i + 1
        ans = ans + char
        if sc > 0 and i == inc:
            ans = ans + sc_val
    
    return ans + "\n"




try:
    
    for i in range(0,500,1):
        
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Connect the socket to the port where the server is listening
        # server_address = ('52.21.1.196', 9090)
        server_address = (args.a, args.p)
        print('connecting to %s port %s' % server_address)
        logging.info('connecting to %s port %s' % server_address)
        sock.connect(server_address)
        
        amount_received = 0
        data_len = 128
        while data_len >= 128:
            data = sock.recv(128)
            data_len = len(data)
            amount_received += data_len
            # print('received "%s"' % data)
            print(bytes(data))
            logging.info(data)
            
        # Send data
        # message = "T".zfill(i*2)
        # message = message + "\n"
        message = get_ans(i)
        # print('sending "%s"' % message)
        print(message)
        logging.info(message)
        sock.sendall(bytearray(message,'UTF-8'))
        
        amount_received2 = 0
        data_len2 = 128
        # while data_len2 >= 128:
        data2 = sock.recv(128)
            # data_len2 = len(data2)
            # amount_received2 += data_len2
        # print('received "%s"' % data2)
        print(bytes(data2))
        logging.info(data2)
        
    

finally:
    print('closing socket')
    logging.info("closing socket")
    sock.close()

# inc = 1
# while True :
#     quest = input()
#     logging.info(quest)
#     ans = get_ans(++inc)
#     print(ans)
#     logging.info(ans)
