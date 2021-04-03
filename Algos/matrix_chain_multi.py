def matrix_chain_order(p):
	n = len(p)
	inf = float('inf')
	m = [[0]*n for i in range(n)]
	s = [[0]*(n) for i in range(n)]

	for i in range(1,n):
		m[i][i] = 0
	for l in range(2,n):
		for i in range(1, n-l+1):
			j = i+l-1
			m[i][j] = inf
			for k in range(i, j):
				q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
				if q < m[i][j]:
					m[i][j] = q
					s[i][j] = k
	return m, s

def print_optimal_parens(s, i, j):
	if i == j:
		print("A"+str(i), end = '')
	else:
		print("(", end = '')
		print_optimal_parens(s, i, s[i][j])
		print_optimal_parens(s, s[i][j] + 1, j)
		print(")", end = '')


p = [30, 35, 15, 5, 10, 20, 25]
min_multiplication, k_value = matrix_chain_order(p)
print(min_multiplication[1][6])
#print(k_value)
print_optimal_parens(k_value, 1, 6)
print()
