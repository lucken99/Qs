from functools import lru_cache
import math


def cherry_pickup(grid):
	m, n = len(grid), len(grid[0])

	# Top down
	# @lru_cache(None)
	# def dp(row, col1, col2):
	# 	if col1 < 0 or col1 >= n or col2 < 0 or col2 >= n:
	# 		return -math.inf

	# 	#current cell
	# 	result = 0
	# 	result += grid[row][col1]
	# 	if col1 != col2:
	# 		result += grid[row][col2]

	# 	# transition
	# 	if row != m-1:
	# 		result += max(dp(row+1, new_col1, new_col2) for new_col1 in [col1, col1+1, col1-1] \
	# 						for new_col2 in [col2, col2+1, col2-1])
	# 	return result

	# return dp(0, 0, n-1)



	# Bottom up

	dp = [[[0]*n for _ in range(n)] for __ in range(m)]

	for row in reversed(range(m)):
		for col1 in range(n):
			for col2 in range(n):
				result = 0

				# current cell
				result += grid[row][col1]
				if col1 != col2:
					result += grid[row][col2]

				# transition
				if row != m-1:
					result += max(dp[row+1][new_col1][new_col2] for new_col1 in 
						[col1, col1+1, col1-1]
						for new_col2 in [col2, col2+1, col2-1] 
						if 0 <= new_col1 < n and 0 <= new_col2 < n)
				dp[row][col1][col2] = result
	return dp[0][0][n-1]

grid = [[1,2,3],[4,5,6],[7,8,9]]
print(cherry_pickup(grid))


