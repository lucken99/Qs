def prime_gen(start, end):
	ans = []
	for i in range(start, end):
		if i > 1:
			for j in range(2, i):
				if (i%j == 0):
					break
			else:
				ans.append(i)
	return ans

def solve(n):
	a = prime_gen(0, n)
	p = n
	for i in range(1,len(a)):
		for j in range(1,len(a)):
			if a[i]*a[j] == p:
				return True
	return False
for i in range(int(input())):
		n = int(input())
		print(solve(n))
		

