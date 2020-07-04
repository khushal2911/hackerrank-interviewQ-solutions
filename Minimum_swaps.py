#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    n = len(arr)
    num_of_swaps = 0
    while True:
        no_swaps_done = True
        i = 0
        while True and i < n:
            if arr[i] != i + 1:
                temp = arr[i]
                arr[i], arr[temp - 1] = arr[temp - 1], arr[i]
                num_of_swaps += 1
                no_swaps_done = False
            i += 1
        if no_swaps_done:
            break
    return num_of_swaps
                 
                 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
