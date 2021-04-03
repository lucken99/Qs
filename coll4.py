from bisect import bisect_left, bisect_right
from functools import reduce
for _ in range(int(input())):
	n, e, h, a, b, c = map(int, input().split())
	l = [i for i in range(n+2)]
	ans = []
	for i in range(n+1):
		bis_left = bisect_left(l, (2*n-e-2*i))
		bis_right = bisect_right(l, h-3*i)-1
		# low, hi = 0, len(l)
		# while low < hi:
		# 	mid = (low+hi)//2
		# 	if l[mid] < (2*n-e-2*i):
		# 		low = mid+1
		# 	else:
		# 		hi = mid
		# bis_left = low

		# low, hi = 0, len(l)
		# while low < hi:
		# 	mid = (low+hi)//2
		# 	if h-3*i < l[mid]:
		# 		hi = mid
		# 	else:
		# 		low = mid+1
		# bis_right = low-1
		if bis_right<bis_left or bis_left==n+1:
			continue
		if bis_right==n+1 and bis_right+3*i>h:
			continue
		if c > a:
			if bis_left < n-i:
				z = bis_left
			else:
				z = n-i
		else:
			if bis_right < n-i:
				z = bis_right
			else:
				z = n-i
		o = n-z-i
		if z+2*i >= 2*n-e and z+3*i<=h:
			ans.append(a*o+b*i+c*z)
	if len(ans) == 0:
		print(-1)
	else:
		mini = ans[0]
		mini = reduce(min, ans)
		print(mini)
		