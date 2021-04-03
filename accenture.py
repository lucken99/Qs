import sys
input = sys.stdin.readline

# for _ in range(int(input())):
	# n = int(input())
	# a = list(map(int, input().split()))
	# ans = 0
	# for i in range(n-1):
	# 	if a[i] > a[i+1]:
	# 		a[i+1] = a[i]
	# 		ans += 1
	# print(ans)


from itertools import compress
# from functools import lru_cache

def primes(n):
    """ Returns  a list of primes < n for n > 2 """
    sieve = bytearray([True]) * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = bytearray((n-i*i-1)//(2*i)+1)
    return [2,*compress(range(3,n,2), sieve[1:])]
j = primes(2*(10**3)+1)

def sieve(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
          
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
              
            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    return prime

prime = sieve(2*(10**6)+1)
prime[0] = False
prime[1] = False
# print(prime)
a = [0]*(2*(10**6) +1)
a[0] = 0
a[1] = 0
a[2] = 1
# @lru_cache(None)
def f(x):
	# nonlocal a
	if prime[x]:
		a[x] = 1
		return
	for i in j:
		if x%i == 0:
			a[x] = x//i*a[i] + i*a[x//i]
			break
for i in range(3, 2*(10**6)+1):
	f(i)
# print(a)

import math
 
# method to print the divisors
def factors(n) :
     
    # Note that this loop runs till square root
    ans = 0
    i = 1
    while i <= math.sqrt(n):
         
        if (n % i == 0) :
             
            # If divisors are equal, print only one
            if (n / i == i) :
                ans += a[i]
            else :
                # Otherwise print both
                ans += a[i]; ans += a[n//i]
        i = i + 1
    return ans

for _ in range(int(input())):
	l, r = map(int, input().split())
	# nonlocal prime
	ans = 0
	for i in range(l, r+1):
		if prime[i]:
			ans += 1
		else:
			ans += factors(i)
	print(ans)


