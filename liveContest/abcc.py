# for _ in range(int(input())):
# 	s = input()
# 	a = ""
# 	for i in s:
# 		a = a+str(int(i)-2)
# 	print(a)

for t in range(int(input())):
	print("Test case:", t+1)
	n = input()
	q = int(input())
	temp = ""
	for i in range(q):
		qu = input()
		if qu[1] == '+':
			ans = 0
			for j in n:
				#temp += str(int(j)+int(qu[0]))[-1]
				ans += int(j) + int(qu[0])
			print(ans)
			n = str(int(n)+int(qu[0]*len(n)))
		elif qu[1] == '*':
			ans = 0
			for j in n:
				ans += int(j)*int(qu[0])
			print(ans)
		else:
			ans = 0
			if qu[0] == '0':
				print("INVALID INPUT.'0' IS EVIL")
			else:
				for j in n:
					ans += int(j)//int(qu[0])
				print(ans)

