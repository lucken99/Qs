import sys
# from math import sqrt
input = sys.stdin.readline
n = (10**6)+1
isprime = [True for i in range(n+1)]
p = 2
while (p*p <= n):
	if isprime[p]:
		for i in range(p*2, n+1, p):
			isprime[i] = False
	p += 1
isprime[0] = 0
isprime[1] = 0
count = 0
for i in range(2, n+1):
	if isprime[i]:
		count += 1
	isprime[i] = count

# print(isprime)
for _ in range(int(input())):
    x, y = map(int, input().split())
    c = isprime[x]
    if c <= y:
        print("Chef")
    else:
        print("Divyam")
