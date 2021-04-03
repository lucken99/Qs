def solve(arr, n):
	arr = arr[:]
	if n == 0:
		return 0

	arr[0] = max(0, arr[0])
	if n == 1:
		return arr[0]
	arr[1] = max(arr[0], arr[1])
	for i in range(2, n):
		arr[i] = max(arr[i-1], arr[i]+arr[i-2])
	return arr
arr = [3, 7, 4, 6, 5]
#arr = [3, 5, -7, 8, 10]
print(solve(arr, len(arr)))
print(arr)