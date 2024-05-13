#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    n = len(s)
    c = math.ceil(math.sqrt(n))
    r = math.floor(math.sqrt(n))

    encryp = ''

    for i in range(c):
        tmp = ''
        for j in range(r+1):
            idx = j * c + i
            if idx < n:
                tmp += s[idx]
        encryp += tmp + ' '

    return encryp


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result)
    fptr.close()