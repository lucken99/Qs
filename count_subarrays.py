def count_sub(n, a):
	# if n <= 1:
	# 	return n
	# elif a[n-1] >= a[n-2]:
	# 	return count_sub(n-1, a) + n
	# else:
	# 	return count_sub(n-1,a) + 1

	s = [0 for i in range(n)]
	s[0] = 1
	for i in range(1,n):
		if a[i] >= a[i-1]:
			s[i] = s[i-1] + 1
		else:
			s[i] = 1
	return sum(s)
t = int(input())
while t:
	t -= 1
	n = int(input())
	a = list(map(int, input().split()))
	print(count_sub(n, a))
