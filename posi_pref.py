for _ in range(int(input())):
	n, k = map(int, input().split())
	a = list(range(n+1))
	i = 1
	sum = 0
	while i <= n:
		if (k == 0) or (k == n):
			break
		if (sum+1 <= i + 1) and k > 0:
			a[i] = i
			sum += i
			i += 1
			k -= 1
			continue
		if sum > i:
			a[i] = -i
			sum -= i
			i += 1
			if sum > 0:
				k -= 1
			continue
		if (sum+1 > (i+1)) and k == 1:
			a[i] = -i
			i += 1
			if sum-i > 0:
				break
			else:
				sum -= i
				continue
		if sum+i > i+1 and k > 1:
			a[i] = i
			if sum > 0:
				k -= 1
			sum += i
			i += 1

	if k == n:
		for i in range(1, n+1):
			a[i] = i
	elif i <= n:
		for j in range(i, n+1):
			a[j] = -j
	for i in range(1, n+1):
		print(a[i], end=" ")
	print()

