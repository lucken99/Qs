import math 
  
def highestPowerof2(n): 
  
    p = int(math.log(n, 2)) 
    return int(pow(2, p))

for _ in range(int(input())):
	n, x   = map(int, input().split())
	a = list(map(int, input().split()))

	c = 0
	y = 0
	for i in a:
		c += bin(i).count('1')
		y ^= i
	# print(y, c)
	c -= bin(a[-1]).count('1')
	if x > c:
		if n == 2 and (x-c)&1:
			print(1, y^1)
		else:
			print("0 "*(n-1), y, sep="")
	else:
		z = 0
		i = 0

		while (z < x) and (i < n):
			if a[i] == 0:
				i += 1
				continue
			p = highestPowerof2(a[i])
			for j in range(i+1, n):
				if a[j]^p < a[j]:
					a[j] ^= p
					a[i] ^= p
					z += 1
					break
				elif j == n-1:
					a[j] ^= p
					a[i] ^= p
					z += 1
					break
			if i == n-1:
				break

		r = x - z
		if r and n == 2:
			if r&1:
				a[0] = 1
				a[1] ^= 1
		print(" ".join(str(i) for i in a))



