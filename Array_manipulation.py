#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0]*n
    max_sum = 0
    x = 0
    for query in queries:
        p = query[0]
        q = query[1]
        incr = query[2]
        arr[p-1] +=incr
        if q<n: arr[q] -= incr
    for i in range(n):
        x += arr[i]
        if max_sum < x:
            max_sum = x
    return max_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
