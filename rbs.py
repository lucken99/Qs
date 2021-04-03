# for _ in range(int(input())):
# 	s = input()
# 	q = s.count('?')
# 	if s[0] == ')':
# 		print("NO")
# 	elif s[-1] == '(':
# 		print("NO")
# 	elif q&1:
# 		print("NO")
# 	else:
# 		print("YES")

	
for _ in range(int(input())):
	n = int(input())
	r = list(map(int, input().split()))
	m = int(input())
	b = list(map(int, input().split()))
	c = r + b
	s = sum(r+b)
	maxi = max(0, s)
	for i in range((m+n)-1, -1, -1):
		s -= c[i]
		maxi = max(maxi, s)

	print(maxi)


