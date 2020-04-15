"""
coin_flips.py -- keep doing N=1000 coin flips and print result
"""

import random
import sys

N = 1000

print("heads")

while True:
    heads = 0
    for i in range(N):
        coin_flip = random.choice([0,1])
        heads += coin_flip
    print(heads)
    sys.stdout.flush()
