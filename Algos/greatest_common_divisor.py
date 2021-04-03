#Euclidian Algorithm
# O(Log(min(a, b)))

def gcd(a, b):
	if a == 0:
		return b
	# elif a%b == 0:
	# 	return b
	else:
		return gcd(b%a, a)

#print(gcd(1000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000000250067694233333335, 1000000000000000000000000000014254123333333333150))

# Extended Euclidian Theorem

# finds integer coefficient of x and y such that:
# ax + by = gcd(a, b)

def extended_gcd(a, b):
	if a == 0:
		return b, 0, 1
	gcd, x1, y1 =  extended_gcd(b%a, a)

	#update x and y using results of recursive call
	x = y1 - (b//a) * x1
	y = x1

	return gcd , x, y

#print(extended_gcd(35, 15))