from functools import wraps

def memo(func):
	cache = {}
	@wraps(func)
	def wrap(*args):
		if args not in cache:
			cache[args] = func(*args)
		return cache[args]
	return wrap

@memo
def lis(arr):
	n = len(arr)

	lis = [1]*n

	for i in range(1, n):
		for j in range(0, i):
			if arr[i] >= arr[j] and lis[i]<lis[j]+1:
				lis[i] = lis[j]+1

	maximum = max(lis)
	# for i in range(n):
	# 	maximum = max(maximum, lis[i])
	return maximum

# using LCS to solve this problem
@memo
def solve(a, b, m, n):
	if m == 0 or n == 0:
		return 0
	elif a[m-1] == b[n-1]:
		return 1+solve(a, b, m-1, n-1)
	return max(solve(a, b, m, n-1), solve(a, b, m-1, n))

a = (10, 22, 9, 33, 21, 50, 41, 60 )
b = tuple(sorted(a))
print(solve(a, b, len(a), len(b)))
print(lis((10, 22, 9, 33, 21, 50, 41, 60)))



