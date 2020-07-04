#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    n = len(q)
    swaps = 0
    i = n-1
    flag = 0
    while(i>=0):
        if q[i]-(i+1) > 2:
            print('Too chaotic')
            flag =1
            break
        else:
            j = max(0,q[i]-2)
            while(j<i):
                if q[j]>q[i]:
                    swaps += 1    
                j += 1 
        i -= 1
    if flag==0:
        print(swaps)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
