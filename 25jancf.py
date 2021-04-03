from sys import stdin


def readint():
	return int(stdin.readline())

def readarray(typ):
	return list(map(typ, stdin.readline().split()))


# def isPowerOfTwo (x):
 
#     # First x in the below expression 
#     # is for the case when x is 0 
#     return (x and (not(x & (x - 1))) )

# for _ in range(readint()):
# 	n = readint()
# 	# a = readarray(int)
# 	# print(*a)
# 	if n&1:
# 		print("YES")
# 	else:
# 		if isPowerOfTwo(n):
# 			print("NO")
# 		else:
# 			print("YES")


# for _ in range(readint()):
# 	n = readint()
# 	q = n//2020
# 	r = n%2020
# 	if r <= q:
# 		print("YES")
# 	else:
# 		print("NO")