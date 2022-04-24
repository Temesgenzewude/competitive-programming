#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    target = arr[n - 1]
    k = n - 2
    while k >= -1:
        if target < arr[k] and k >= 0:
            arr[k + 1] = arr[k]
            for j in range(n):
                if (j + 1) % n == 0:
                    print(arr[j])
                else:
                    print(arr[j], end=' ')
        else:
            arr[k + 1] = target
            for j in range(n):
                if (j + 1) % n == 0:
                    print(arr[j])
                else:
                    print(arr[j], end=' ')
            break
        k -= 1


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

