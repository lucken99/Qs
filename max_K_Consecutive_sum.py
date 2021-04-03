def max_k_consecutive_sum_array(a, k, n):
	sums = 0
	for i in range(k):
		sums += a[i]
	maxi = sums
	for i in range(k,n):
		sums = (sums - a[i-k]) + a[i]
		maxi = max(maxi, sums)
	return maxi

a = [5, -1, -1, 0, 3, -10, -10, 2, -10]
print(max_k_consecutive_sum_array(a, 3, len(a)))
