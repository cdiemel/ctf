#!/usr/bin/python3
__author__ = 'C. Diemel'
__version__ = '1.0.0'
__name__ = 'hidden_add.py'
__license__ = 'GPL2'
__description__ = 'Read from cli, eval, print.'


import logging
import time

logging.basicConfig(filename='add.log', filemode='w', level=logging.DEBUG)
# logging.basicConfig(filename='add.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
# logging.debug('This will get logged to a file')
# logging.info('This will get logged to a file')
# logging.warning('This will get logged to a file')
# logging.error('This will get logged to a file')

for i in range(0,3,1):
    text = input()
    time.sleep(1)
    logging.info(text)
    time.sleep(1)

# for i in range(0,100,1):
while True :
    prob = input()
    logging.info(prob)
    ans = eval(prob)
    # time.sleep(0.25)
    print(ans)
    msg = ("%s ans: %s" % (prob, ans))
    logging.info(ans)
    # time.sleep(0.25)
