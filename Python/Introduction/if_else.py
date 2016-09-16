#!/bin/python3

import sys

n = int(input().strip())

if n % 2 == 1:
    print('Weird')
elif n < 5 or n > 20:
    print('Not Weird')
else:
    print('Weird')