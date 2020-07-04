#!/bin/python3

import math
import os
from collections import defaultdict
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    temp = defaultdict(int)
    for i in range(n):
        temp[ar[i]] += 1
    result = sum([i//2 for i in temp.values()])
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
