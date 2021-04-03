
# import math

# vaccine
# d1, v1, d2, v2, p = map(int, input().split())
# days = 0
# vaccine = 0
# if d1 == d2:
# 	print((min(d1, d2)-1) + math.ceil(p/(v1+v2)))

# else:
# 	if d2 < d1:
# 		d1, d2 = d2, d1
# 		v1, v2 = v2, v1
# 	if math.ceil(p/v1) <= (d2-d1):
# 		print(d1-1 + math.ceil(p/v1))

# 	else:
# 		print(d1-1 + (d2-d1) + math.ceil(p-v1*(d2-d1) / (v2+v1))





# Even Pair Sum
# for _ in range(int(input())):
# 	a, b = map(int, input().split())
# 	even_a = a//2
# 	odd_a = math.ceil(a/2)
# 	even_b = b//2
# 	odd_b = math.ceil(b/2)
# 	print((even_a*even_b) + (odd_a*odd_b))



# Vaccine Distribution
# for _ in range(int(input())):
# 	n, d = map(int, input().split())
# 	a = list(map(int, input().split()))

# 	b = [i for i in a if i >= 80 or i <= 9]
# 	a1 = [i for i in a if i<80 and i > 9]
# 	print(math.ceil(len(b)/d) + math.ceil(len(a/d)))




# Positive Prefixes
# for _ in range(int(input())):
# 	n, k = map(int,input().split())
# 	a = []
# 	for i in range(1, n+1):
# 		if i&1:
# 			a.append(-i)
# 		else:
# 			a.append(i)
	
# 	if k == n:
# 		print(" ".join(str(i) for i in range(1, n+1)))
# 	elif k == n//2:
# 		print(" ".join(str(i) for i in a))
# 	elif k > n//2:
# 		z = k - n//2
# 		i = -1
# 		while z:
# 			if a[i]&1:
# 				a[i] = -a[i]
# 				z -= 1
# 				i -= 2
# 			else:
# 				i -= 1
# 		print(" ".join(str(i) for i in a))
# 	else:
# 		z = n//2 - k
# 		i = -1
# 		while z:
# 			if a[i]&1:
# 				i -= 1
# 			else:
# 				a[i] = -a[i]
# 				z -= 1
# 				i -= 2
# 		print(" ".join(str(i) for i in a))




#  Hail XOR

# import math 
  
# def highestPowerof2(n): 
  
#     p = int(math.log(n, 2)) 
#     return int(pow(2, p))

# for _ in range(int(input())):
# 	n, x   = map(int, input().split())
# 	a = list(map(int, input().split()))

# 	c = 0
# 	y = 0
# 	for i in a:
# 		c += bin(i).count('1')
# 		y ^= i
# 	# print(y, c)
# 	c -= bin(a[-1]).count('1')
# 	if x > c:
# 		if n == 2 and (x-c)&1:
# 			print(1, y^1)
# 		else:
# 			print("0 "*(n-1), y, sep="")
# 	else:
# 		z = 0
# 		i = 0

# 		while (z < x) and (i < n):
# 			if a[i] == 0:
# 				i += 1
# 				continue
# 			p = highestPowerof2(a[i])
# 			for j in range(i+1, n):
# 				if a[j]^p < a[j]:
# 					a[j] ^= p
# 					a[i] ^= p
# 					# print(a[i])
# 					z += 1
# 					break
# 				elif j == n-1:
# 					a[j] ^= p
# 					a[i] ^= p
# 					# print(a[i])
# 					z += 1
# 					break
# 			if i == n-1:
# 				break

# 		r = x - z
# 		if r and n == 2:
# 			if r&1:
# 				a[0] = 1
# 				a[1] ^= 1
# 		print(" ".join(str(i) for i in a))



# String Operations
for _ in range(int(input())):
	s = input()
	n = len(s)
	a = set()
	for i in range(n):
		temp = ""
		for j in range(i, n):
			temp += s[j]
			a.add(temp)
	b = [i for i in a]
	b.sort(key=lambda x: len(x))
	

	# print(b)


	# print(" ".join(a), "length",len(a))
	print(len(a))















	