import sys

input = sys.stdin.readline

def solve(a = None, n=None, k=None):
	ans = 0
	# print(a)
	return ans

for _ in range(int(input())):
	# n = int(input())
	# n, k = map(int, input().split())
	# a = list(map(int, input().split()))
	n, m, x = map(int, input().split())
	q = x//n
	r = x%n
	if r == 0:
		print((n-1)*m+q)
	else:
		r -= 1
		print(m*r + q + 1)

	# print(solve(a, n))

