import sys
input = sys.stdin.readline
import math
for _ in range(int(input())):
	n = int(input())
	z = ((1 << int(math.log2(n))) - 1)
	print(z* (n^z))

# for _ in range(int(input())):
# 	n, e, h, a, b, c = map(int, input().split())
# 	poss = 0
# 	mini = e
# 	if e >= h:
# 		poss = h + (e-h)//2
# 		mini = h
		
# 	else:
# 		poss = e + (h-e)//3

# 	if n > poss:
# 		print(-1)
# 	# elif n == poss:
# 	# 	if mini == e:
# 	# 		print(e*c + b*((h-e)//3))
# 	# 	else:
# 	# 		print(h*c + a*((e-h)//2))
# 	elif n == e == h:
# 		print(c*n)
# 	else:
# 		q = [(a, 2), (b, 3), (c, 1)]
# 		q.sort()
# 		ans = 0
# 		i = 0
# 		cost = 0
# 		while i < 3 and n:
# 			if q[i][1] == 2:
# 				ans += e//2
# 				cost += a*min((e//2), n)
# 				n -= min(e//2, n)
# 				e -= (e//2)*2
# 			elif q[i][1] == 3:
# 				ans += h//3
# 				cost += b*min((h//3), n)
# 				n -= min(h//3, n)
# 				h -= (h//3)*3
# 			else:
# 				ans += min(e, h)
# 				cost += c*min(min(e, h), n)
# 				n -= min(min(e, h), n)
# 				e -= min(e, h)
# 				h -= min(e, h)
# 			i += 1
# 		print(cost)



