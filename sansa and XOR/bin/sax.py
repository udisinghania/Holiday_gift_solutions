#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sansaXor function below.
def sansaXor(arr):
    p=len(arr)
    l=[]
    k=1
    for i in range (p):
        t=arr[i]
        l.append(t)
        for j in range (i+1,p):
            t=t^arr[j]
            l.append(t)
    y=l[0]
    for i in range (1,len(l)):
        y=y^l[i]
    return y       

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = sansaXor(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
