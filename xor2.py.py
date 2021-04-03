#!/bin/python3

import os

LOGM = 16
M = 2**16
freqs = [0]*M

#
# Complete the xorSubsequence function below.
#
def xorSubsequence(a):
    #
    # Write your code here.
    #
    acc = 0;
    freqs[0] += 1
  
    for i in range(a_count):
        acc ^= a[i]
        freqs[acc] += 1
        
    xorConvolution()
  
    y = 0;
    
    for i in range(1,M):    
        if (freqs[i] > y):
            y = freqs[i]
            x = i

    return [x, y//2]

def xorConvolution():
    walsh_dit2()
    for i in range(M):
        freqs[i] *= freqs[i]
    walsh_dit2()
    for i in range(M):
        freqs[i] //= M

def orConvolution():
    arith()
  
    for i in range(M):
        freqs[i] *= freqs[i]
    
    arith_minus()

def walsh_dit2():
    m = 2
    
    while m <= M:
        mh = m // 2
        for i in range(0,M,m):
            for j in range(mh):              
                x = freqs[i+j]
                y = freqs[i+j+mh]
                freqs[i+j] = x+y
                freqs[i+j+mh] = x-y
        m *= 2

def arith():
    m = 2
    
    while m <= M:
        mh = m // 2
        for i in range(0,M,m):
            for j in range(mh):              
                x = c[i+j]
                y = c[i+j+mh]
                freqs[i+j] = x
                freqs[i+j+mh] = x-y
        
        m *= 2

def arith_minus():
    m = 2
    
    while m <= M:
        mh = m // 2
        for i in range(0,M,m):
            for j in range(mh):              
                x = freqs[i+j]
                y = freqs[i+j+mh]
                freqs[i+j] = x
                freqs[i+j+mh] = y-x
        
        m *= 2

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # a_count = int(input())

    # a = []
    a = [1,3,5,2]
    a_count = len(a)

    

    result = xorSubsequence(a)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
