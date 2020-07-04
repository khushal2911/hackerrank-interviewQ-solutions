#!/bin/python3

import math
import os
import random
from collections import defaultdict
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    c = len(a)
    d = len(b)
    ma = max(c,d)
    mi = min(c,d)
    e = defaultdict(int)
    f = defaultdict(int)
    for i in range(ma):
        if i<mi:
            e[a[i]] += 1
            f[b[i]] += 1
        elif i>c-1:
            f[b[i]] += 1
        else:
            e[a[i]] += 1
    count = 0        
    common = list(set(e.keys()).intersection(set(f.keys())))
    for key in common:
        count += abs(e[key] - f[key])
    noncommon = list(set(e.keys()) ^ set(f.keys()))
    for key in noncommon:
        if key in e.keys():
            count += e[key]
        else:
            count += f[key]
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
