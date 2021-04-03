# Given an array of integers of size ‘n’.
# Our aim is to calculate the maximum sum of ‘k’ 
# consecutive elements in the array.

# Input  : arr[] = {100, 200, 300, 400}
#          k = 2
# Output : 700

# Input  : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}
#          k = 4 
# Output : 39
# We get maximum sum by adding subarray {4, 2, 10, 23}
# of size 4.

# Input  : arr[] = {2, 3}
#          k = 3
# Output : Invalid
# There is no subarray of size 3 as size of whole
# array is 2.

def max_consecutive_sum(arr, k):
	n = len(arr)
	max_sum = 0
	sliding_win = 0

	if k > n:
		return -1

	sliding_win = sum(arr[:k])

	max_sum = sliding_win
	for i in range(k,n):
		sliding_win = sliding_win + arr[i] - abs(arr[i-k])
		max_sum = max(sliding_win, max_sum)

	return max_sum

arr = [1, 4, 2, 10, 20, 4, 3, 0, 20]
k = 4
print(max_consecutive_sum(arr, k))


