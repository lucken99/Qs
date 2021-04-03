#Rod-cutting



# import sys
# sys.setrecursionlimit(10**9)
# Recursive Top-down Implementation
# def memoization(func):
# 	memory = {}
# 	def inner(num, p):
# 		if num not in memory:
# 			memory[num] = func(num, p)
# 		return memory[num]
# 	return inner

# @memoization
# def rod_cutting(n, p):
# 	if n == 0:
# 		return 0
# 	q = float('-inf')
# 	for i in range(1,n+1):
# 		q = max(q, p[i-1] + rod_cutting(n-i, p))
# 	return q

# p = list(map(int, input().split()))


# #p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
# n = len(p)
# print(rod_cutting(n, p))


# Recursive top-down implementation Cormen

# def memoized_cut_rod(p, n):
# 	elem = float('-inf')
# 	r = [elem for i in range(n+1)]
# 	return memoized_cut_rod_aux(p, n, r)

# def memoized_cut_rod_aux(p, n, r):
# 	if r[n] >= 0:
# 		return r[n]
# 	if n == 0:
# 		q = 0
# 	else:
# 		q = float('-inf')
# 		for i in range(1,n+1):
# 			q = max(q, p[i-1] + memoized_cut_rod_aux(p, n-i, r))
# 	r[n] = q
# 	return q
# #p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
# p = list(map(int, input().split()))
# n = len(p)
# print(memoized_cut_rod(p, n))


# Bottom-up cut-rod

# def bottom_up_cut_rod(p, n):
# 	r = [0 for i in range(n+1)]
# 	for j in range(1, n+1):
# 		q = float('-inf')
# 		for i in range(1, j+1):
# 			q = max(q, p[i-1]+r[j-i])
# 		r[j] = q
# 	return r[n]

# #p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
# p = list(map(int, input().split()))
# n = len(p)
# print(bottom_up_cut_rod(p, n))


# Actual Solution of cutting rod (bottom up)

def extended_bottom_up_cut_rod(p, n):
	r = [0 for i  in range(n+1)]
	s = [0 for i in range(n+1)]
	for j in range(1, n+1):
		q = float('-inf')
		for i in range(1,j+1):
			if q < p[i-1] + r[j-i]:
				q = p[i-1]+r[j-i]
				s[j] = i
		r[j] = q
	return r,s

def print_cut_rod_solution(p, n):
	r,s = extended_bottom_up_cut_rod(p, n)
	while n > 0:
		print(s[n])
		n -= s[n]

p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
#p = list(map(int, input().split()))
n = len(p)
print_cut_rod_solution(p, n)


# modified rod-cutting in which 
#in addition to a
#price p i for each rod, each cut incurs a fixed cost of c
# i.e., the The revenue associated with
# a solution is now the sum of the prices of the pieces
# minus the costs of making the cuts
# 
def extended_bottom_up_cut_rod_with_fixed_cost(p, n, cost):
	r = [0 for i  in range(n+1)]
	s = [0 for i in range(n+1)]
	for j in range(1, n+1):
		q = float('-inf')
		for i in range(1,j+1):
			if q < p[i-1] + r[j-i] - cost:
				q = p[i-1]+r[j-i] -cost 
				s[j] = i
		r[j] = q
	return r,s

def print_cut_rod_solution_with_fixed_cost(p, n, cost):
	r,s = extended_bottom_up_cut_rod_with_fixed_cost(p, n, cost)
	while n > 0:
		print(s[n])
		n -= s[n]

p = [1, 5, 8, 9, 10, 17, 17]#, 20, 24, 30]
#p = list(map(int, input().split()))
n = len(p)
cost = 2
print_cut_rod_solution_with_fixed_cost(p, n, cost)