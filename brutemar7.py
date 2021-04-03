import sys
input = sys.stdin.readline
import math
for _ in range(int(input())):
	n = int(input())
	maxi = 0
	z = 1 << (int(math.log2(n)) + 1)
	# print(z)
	for i in range(1, z):
		for j in range(1, z):
			if i^j == n:
				maxi = max(i*j, maxi)
	print(maxi)