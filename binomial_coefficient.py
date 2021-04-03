def binomial_coeff(n, m):
	bc = [[0 for i in range(n+1)] for j in range(n+1)]
	for i in range(n+1):
		bc[i][0] = 1
	for i in range(n+1):
		bc[i][i] = 1
	for i in range(1,n+1):
		for j in range(1,i):
			bc[i][j] = bc[i-1][j-1] + bc[i-1][j]
	
	return bc[n][m]


print(binomial_coeff(1000,10))
