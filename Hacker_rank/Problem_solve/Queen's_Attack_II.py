#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def move(n, r_q, c_q, rMove, cMove, obstacles):
    answer = 0

    r_q += rMove
    c_q += cMove

    while 0 < r_q <= n and 0< c_q <= n:
        if r_q * n + c_q not in obstacles:
            answer += 1
        else:
            break
        r_q += rMove
        c_q += cMove

    return answer

def queensAttack(n, k, r_q, c_q, obstacles):
    answer = 0
    d = [[1,-1], [1,0], [1,1], [0, -1], [0, 1], [-1, -1], [-1, 0], [-1, 1]]
    obs = {r * n + c : None for r,c in obstacles}

    for r, c in d:
        answer += move(n, r_q, c_q, r, c, obs)

    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])

    r_qC_q = input().split()
    r_q = int(r_qC_q[0])
    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result))
    fptr.close()