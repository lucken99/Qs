for _ in range(int(input())):
	n, e, h, a, b, c = map(int, input().split())
	ans = -1
	mini = float('INF')
	if e//2 >= n:
		mini = min(a*min(n, (e//2)), mini)
	if h//3 >= n:
		mini = min(mini, b*min(h//3, n))
	if min(h, e) >= n:
		mini = min(mini, c*(min(h,e,n)))
	if e//2 + h//3 >= n:
		if a <= b:
			mini = min(mini, a*(e//2) + b*(n-e//2))
		else:
			mini = min(mini, b*(h//3)+a*(n-h//3))
	if 



	# poss = 0
	# mini = e
	# if e >= h:
	# 	poss = h + (e-h)//2
	# 	mini = h
		
	# else:
	# 	poss = e + (h-e)//3

	# if n > poss:
	# 	print(-1)
	# elif n == e == h:
	# 	print(c*n)
	# else:
		
