# t = int(input())
# while t:
#   t -= 1

#   m, n = map(int, input().split())
#   for i in range(m, n+1):
#       if i > 1:
#           for n in range(2, i//2 + 2):
#               if i%n == 0:
#                   break
#               else:
#                   if n == i//2 + 1:
#                       print(i)
#   print()


# Sieve Of Erastosthenes Algorithmn O(n*log(log(n)))

# def SieveOfErastothenes(n):

#     # Create a boolean array "prime[0..n]" and initialize 
#     #  all entries it as true. A value in prime[i] will 
#     # finally be false if i is Not a prime, else true.

#     prime = [True for i in range(n+1)]

#     p = 2

#     while (p * p <= n):

#       # if prime[p] is not changed, then it is prime
#       if prime[p] == True:

#           # updates all multiples of p
#           for i in range(p * p, n+1, p):
#               prime[i] = False
#       p += 1
#     # print all prime numbers
#     for p in range(n+1):
#       if prime[p]:
#           print(p)

# SieveOfErastothenes(10000)


# Segmented Sieve for large numbers and for a range of numbers

from math import floor, sqrt

# This functions finds all primes smaller than limit  
# using simple sieve of eratosthenes.  It stores found  
# primes in list prime[]

def simpleSieve(limit, primes):
    mark = [False]*(limit+1)

    for i in range(2, limit+1):
        if not mark[i]:
            # if not marked yet, then its a prime
            primes.append(i)
            for j in range(i, limit+1, i):
                mark[j] = True

# find all prime numbers in a givn range using segmented sieve

def primesInRange(low, high):

    # Comput all primes smaller or equal to  
    # square root of high using simple sieve.

    limit = floor(sqrt(high)) + 1
    primes = list()
    simpleSieve(limit, primes)

    ran = high - low + 1

    mark = [False]*(ran+1)

     # Use the found primes by simpleSieve() to find  
    # primes in given range

    for i in range(len(primes)):
        # Find the minimum number in [low..high] that is  
        # a multiple of prime[i] (divisible by prime[i]) 

        loLim = floor(low/primes[i]) * primes[i]
        if loLim < low:
            loLim += primes[i]
        if loLim == primes[i]:
            loLim += primes[i]

        # Mark multiples of primes[i] in [low..high]:   
        # We are marking j - low for j, i.e. each number   
        # in range [low, high] is mapped to [0, high-low]   
        # so if range is [50, 100] marking 50 corresponds   
        # to marking 0, marking 51 corresponds to 1 and   
        # so on. In this way we need to allocate space   
        # only for range

        for j in range(loLim, high+1, primes[i]):
            mark[j-low] = True

    # Numbers which are not marked in range, are prime
    for i in range(low, high+1):

        if not mark[i-low] and i != 1:
            print(i)


primesInRange(999900000, 1000000000)

# t = int(input())
# while t:
#     t -= 1
#     m, n = map(int, input().split())
#     primesInRange(m, n)
#     print()