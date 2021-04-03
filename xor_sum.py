import sys
from math import comb
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
q = int(input())
l = len(f"{max(a):b}")
b = []

for i in range(l):
	ones = 0
	zeros = 0
	for j in range(n):
		if a[j]&1:
			ones += 1
		else:
			zeros += 1
		a[j] >>= 1
	b.append([ones, zeros])
print(b)
ans = [0]*(n+1)

p = [0]*l

for i in range(q):
	m = int(input())
	if ans[m] 

