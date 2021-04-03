from math import ceil
def f(n, k, l):
	a = []
	for i in range(l):
		for j in range(1, k+1):
			if n == 0:
				return a
			a.append(j)
			n -= 1
	return a
for _ in range(int(input())):
	a = []
	n, k, l = map(int, input().split())
	if k*l < n or (k == 1 and n > 1):
		print(-1)
	else:
		s = f(n, k, l)
		print(" ".join(str(i) for i in s))





	