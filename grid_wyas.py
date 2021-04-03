

# for _ in range(int(input())):
# 	n, m = map(int, input().split())
# 	grid = []
# 	MOD  = 1000000007
# 	for i in range(n):
# 		z = input()
# 		grid.append([i for i in z])

# 	for i in range(n):
# 		for j in range(m):
# 			if grid[i][j] == '.':
# 				grid[i][j] = 0


# 	grid[0][0] = 1


	# for i in range(0, n):
	# 	for j in range(0, m):
	# 		if grid[i][j] != '*':
	# 			sum = 0
	# 			for k in range(j, 0, -1):
	# 				if grid[i][k] == '*':
	# 					break
	# 				elif grid[i][k-1] != '*':
	# 					sum += grid[i][k-1] % MOD
	# 				else:
	# 					break

	# 			for k in range(i, 0, -1):
	# 				if grid[k][j] == '*':
	# 					break
	# 				elif grid[k-1][j] != '*':
	# 					sum += grid[k-1][j] % MOD
	# 				else:
	# 					break
	# 			grid[i][j] += sum % MOD




	# print(grid)
	# print(grid[-1][-1] % MOD)



MOD = int(1e9 + 7)
# t = int(input())
# while t > 0:
#     t -= 1
#     n, m = map(int, input().split())
#     matrix = []
#     for i in range(n):
#         matrix += [input()]
#     dp = [[0] * m for _ in range(n)]
#     for i in range(n):
#         for j in range(m):
#             if i == 0 and j == 0:
#                 dp[i][j] = 1
#             elif matrix[i][j] == '.':
#                 for k in range(i - 1, -1, -1):
#                     if matrix[k][j] != '.':
#                         break
#                     dp[i][j] = (dp[i][j] + dp[k][j]) % MOD
#                 for k in range(j - 1, -1, -1):
#                     if matrix[i][k] != '.':
#                         break
#                     dp[i][j] = (dp[i][j] + dp[i][k]) % MOD
#     print(dp[n - 1][m - 1])


def num_of_ways_with_obstacles(grid, n, m):
	dp = [[0] * m for _ in range(n)]
	for i in range(n):
	    for j in range(m):
	        if i == 0 and j == 0:
	            dp[i][j] = 1
	        elif grid[i][j] == '.':
	            for k in range(i - 1, -1, -1):
	                if grid[k][j] != '.':
	                    break
	                dp[i][j] = (dp[i][j] + dp[k][j]) % MOD
	            for k in range(j - 1, -1, -1):
	                if grid[i][k] != '.':
	                    break
	                dp[i][j] = (dp[i][j] + dp[i][k]) % MOD
	return dp[n - 1][m - 1]

grid = [['.', '.', '.'], ['.', '*', '.'], ['.', '.', '.']]
n = len(grid)
m = len(grid[0])

print(num_of_ways_with_obstacles(grid, n, m))
