# import numpy as np
import sys
from functools import lru_cache

sys.setrecursionlimit(10**6)
dp = [[0]*4020 for i in range(4020)]
pref = [0]*4020

# dp  = np.zeros((4020, 4020), dtype=int)
# pref = np.zeros(4020, dtype=int)

# @lru_cache
def recur(idx, taken, n, k, arr):
	if taken >= k and (pref[idx]-taken >= k):
		return 0
	elif idx >= n:
		return int(1e10)
	elif dp[idx][taken] != -1:
		return dp[idx][taken]

	c1 = recur(idx+1, min(taken+arr[idx], pref[idx]-taken), n, k, arr)
	c2 = recur(idx+1, min(pref[idx]-taken+arr[idx], taken), n, k, arr)

	dp[idx][taken] = 1+min(c1, c2)
	return dp[idx][taken]

def dp_solve(arr, n, k):
	for i in range(n//2):
		arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
	for i in range(n+11):
		pref[i] = 0
		for j in range(k+11):
			dp[i][j] = -1
	for i in range(1, n+1):
		pref[i] = pref[i-1]+arr[i-1]
	ans = recur(0, 0, n, k, arr)
	if ans>int(1e9):
		return -1
	else:
		return ans


for _ in range(int(input())):
	n, k = map(int, input().split())
	arr = list(map(int, input().split()))
	arr.sort()
	# arr = tuple(arr)
	if n == 1:
		print(-1)
	else:
		print(dp_solve(arr, n, k))
