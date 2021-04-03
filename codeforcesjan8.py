# for _ in range(int(input())):
# 	n = int(input())
# 	if n == 1:
# 		print(9)
# 	elif n ==2:
# 		print(98)
# 	elif n == 3:
# 		print(989)
# 	elif n == 4:
# 		print(9890)
# 	else:
# 		print(9890, end="")
# 		for i in range(1, n-3):
# 			print(i%10, end="")
# 		print()

for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	ans = 0
	prev = -1
	flag = False
	for i in range(0, n-2):
		x, y, z = a[i], a[i+1], a[i+2]
		if (y > x and y > z) or (y < x and y < z):
			ans += 1
			if (prev+1) and (i-1 == prev):
				flag = True
			else:
				prev = i

	if flag:
		if ans >= 2:
			print(ans-2)
		else:
			print(0)
	else:
		if ans >= 1:
			print(ans-1)
		else:
			print(0)
			

