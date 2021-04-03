def isprime(n):
	if n <= 1:
		return False
	if n <= 3:
		return True

	if (n%2 == 0 or n%3 == 0):
		return False
	i = 5
	while i*i <= n:
		if n%i == 0:
			print(i)
			return False
		if n%(i+2) == 0:
			print(i+2)
			return False
		i += 6
	return True

print(isprime(59))