#!/bin/python3

import math
import os
import random
from collections import defaultdict, Counter
import re
import sys

# Complete the isValid function below.
def isValid(s):
    l = len(s)
    dict_ = defaultdict(int)
    for char in s:
        dict_[char] += 1
    f = set(dict_.values())
    if len(f)>2:
        return 'NO'
    f1 = max(f)
    f2 = min(f)
    count = Counter(dict_.values())
    if f1-f2 > 1 and f2>1:
        return 'NO'
    elif f2==1 and count[f2]>1:
        return 'NO'
    else:
        return 'YES'
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
