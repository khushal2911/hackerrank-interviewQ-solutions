#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    L = len(c)
    steps = 0
    i = 0
    while(i<L-1):
        if i== L-2:
            steps += 1
            break
        elif c[i+2]:
            i += 1
        else :
            i += 2
        steps += 1
    return steps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
