#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(arr):
    swap = 0
    for k in range(1, len(arr)):
        for i in range(len(arr) - k):
            j = i + 1
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                swap += 1
    print("Array is sorted in", swap, "swaps.")
    print("First Element:", arr[0])
    print("Last Element:", arr[-1])

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
