# import sys
# sys.setrecursionlimit(10**9)
# def memoize_num(func):
# 		memory = {}

# 		def inner(x):
# 			if x not in memory:
# 				memory[x] = func(x)
# 			return memory[x]

# 		return inner


# @memoize_num
# def points(x):
# 	if x == 1:
# 		return 0
# 	elif x == 2:
# 		return 1
# 	elif x == 3:
# 		return 1
# 	else:
# 		return points(x-2) + points(x-3)



def points(x):
	memory = [0 for i in range(x+1)] # memory = [0]*(10**6 + 1)
	memory[1] = 0
	memory[2] = 1
	memory[3] = 1
	for i in range(4, x+1):
	    memory[i] = (memory[i-2] + memory[i-3])%1000000009
	return memory[x]


t = int(input())
while t:
	t -= 1
	x = int(input())
	res = points(x)
	print(res)
	

