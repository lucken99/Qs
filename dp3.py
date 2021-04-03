import sys
sys.setrecursionlimit(10**6)
# def memoization(func):
# 	memory = {}

# 	def inner(num):
# 		if num not in memory:
# 			memory[num] = func(num)
# 		return memory[num]
# 	return inner

# Recursive approach exponential or NP complete
def isSubsetSum(set_list, n, sum):
	if (sum != 0) and (n==0):
		return False
	if sum == 0:
		return True

	return isSubsetSum(set_list, n-1, sum) or isSubsetSum(set_list, n-1, sum - set_list[n-1])

# using dynamic programming and making it pseudo polynomial
def isSubsetSum1(set_list, n, sum):
	subset = ([[False for i in range(sum+1)] for i in range(n+1)])

	#if sum is 0, then answer is true
	for i in range(n+1):
		subset[i][0] = True

	# if sum is not 0 and set is empty,
	# then answer is false
	for i in range(1, sum+1):
		subset[0][i] = False

	# Fill the subset table in bootom up manner
	for i in range(1, n+1):
		for j in range(1, sum+1):
			if j<set_list[i-1]:
				subset[i][j] = subset[i-1][j]
			if j>= set_list[i-1]:
				subset[i][j] = (subset[i-1][j] or subset[i-1][j-set_list[i-1]])
	return subset[n][sum]

set_list = [3, 34, 4, 12, 5, 2,4,7,5,7,6,8,9,7,2,75,65,7777,87547,5869874,47,1524,475,586,254,14785,254,1452,257,1254]
sum = 25714
n = len(set_list)
a = isSubsetSum1(set_list, n, sum)
print(a)

# solve = memoization(solve)



