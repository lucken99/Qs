def max_subarray_sum(arr):
	sum = 0
	best = 0
	for i in range(len(arr)):
		sum = max(arr[i], sum+arr[i])
		best = max(best, sum)
	return best

print(max_subarray_sum([-1, 2, 4, -3, 5, 2, -5, 2]))

