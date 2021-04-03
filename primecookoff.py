import sys
from math import sqrt
input = sys.stdin.readline
# t=int(input())
t = 10**6
def s(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    return prime
def c(N,isPrime):
    ans=[0]
    for i in range(2, N + 1, 1):
        if (isPrime[i] and isPrime[i - 2]):
            ans.append(ans[-1]+1)
        else:
            ans.append(ans[-1])
 
    return ans
isPrime=s(1000001)
ans=c(1000001,isPrime)
print(ans)

# for _ in range(int(input())):
#     x, y = map(int, input().split())
#     c = ans[x-1]
#     if c <= y:
#         print("Chef")
#     else:
#         print("Divyam")
