#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(scores, alice):
    answer = []

    rank = len(set(scores))+1
    idx = len(scores) -1

    for a in alice:
        while idx >= 0 and scores[idx] <= a:
            rank -= 1
            if idx < len(scores)-1 and scores[idx] == scores[idx+1]:
                rank += 1

            idx -= 1

        answer.append(rank)

    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())
    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())
    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.close()