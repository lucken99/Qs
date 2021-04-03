import sys
input = sys.stdin.readline
import heapq

# n = int(input())
# if n < 0:
# 	print("Wrong Input")
# else:
# 	p = n*n*n*n
# 	# p = str(p)
# 	# l = len(str(n))
# 	# if p[len(p)-l:] == str(n):
# 	# 	print("TRUE")
# 	# else:
# 	# 	print("FALSE")
# 	if p%10**(len(str(n))) == n:
# 		print("TRUE")
# 	else:
# 		print("FALSE")

x = int(input())
a = []
for i in range(x):
	z = int(input().strip())
	a.append(z)
n = int(input())
def ans(a, n, x):
	if len(set(a)) != x:
		print("INVALID INPUT")
	if x == 1:
	    return a[0]
	if n == x:
	    return min(a)

	# the min-heap
	h = []
	for i in range(n):
	    heapq.heappush(h, a[i])

	for i in range(n, x):
	    if a[i] > h[0]:
	        heapq.heappop(h)
	        heapq.heappush(h, a[i])

	return h[0]
print(ans(a, n, x))