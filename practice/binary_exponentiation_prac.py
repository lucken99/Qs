from math import log2
def binary_exponentiatian(a, n):
	copy_n = n
	ans = 1
	while copy_n > 0:
		if copy_n&1:
			ans *= a
		a *= a
		copy_n >>= 1
	return ans


def binary_expo_recursive(a, n):
	if n <= 0:
		return 1
	ans = binary_expo_recursive(a, n//2)
	if n&1:
		return ans * ans * a
	else:
		return ans * ans


# print(binary_exponentiatian(2, 1000))
# print(binary_expo_recursive(2, 1000))

