#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findSubstring' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#
   


def findSubstring(s, k):
    # Write your code here
    vowels = {'a', 'e', 'i', 'o', 'u'}
    ans = 0
    r = 0
    l = 0
    for i in range(len(s)):
        temp = 0
        if k+i <= len(s):
            for j in range(i, k+i):
                if s[j] in vowels:
                    temp += 1
            if temp > ans:
                ans = temp
                l  = i
                r = j+1
    return s[l:r] if len(s[l:r]) !=0 else "Not found!"
        
            
a = 'qwdftr'
b = 'caberqiitefg'
print(findSubstring(a, 2))
