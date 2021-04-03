from sys import stdin, stdout
input = stdin.readline
# print = stdout.write
from random import randint, sample
from itertools import permutations
from math import factorial
# a = []
# print(100)
# for t in range(100):
# 	n = randint(2, 100)
# 	print(n)
# 	a = sample(range(1, n+1), n)
# 	assert len(set(a)) == n
# 	print(*a)
n = 7
a = permutations(range(1, n+1), n)
t = factorial(n)
print(t)
for _ in range(t):
	for i in a:
		print(*i)