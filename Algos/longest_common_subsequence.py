#correct code
def lcs_length(x, y):
	m = len(x)
	n = len(y)
	b = [[0]*(n+1) for i in range(m+1)]
	c = [[0]*(n+1) for i in range(m+1)]

	# for i in range(1, m+1):
	# 	c[i][0] = 0
	# for j in range(n+1):
	# 	c[0][j] = 0
	for i in range(1, m+1):
		for j in range(1, n+1):
			if x[i-1] == y[j-1]:
				c[i][j] = c[i-1][j-1] + 1
				b[i][j] = "↖"
			elif c[i-1][j] >= c[i][j-1]:
				c[i][j] = c[i-1][j]
				b[i][j] = "↑"
			else:
				c[i][j] = c[i][j-1]
				b[i][j] = "⬅"
	return c, b

def print_lcs(b, x, i, j):
	if (i == 0) or (j ==0):
		return
	if b[i][j] == "↖":
		print_lcs(b, x, i-1, j-1)
		print(x[i-1], end = "")
	elif b[i][j] == "↑":
		print_lcs(b, x, i-1, j)
	else:
		print_lcs(b, x, i ,j-1)





# correct code
# def lcs_length(x, y):
# 	m = len(x)
# 	n = len(y)
# 	c = [[0]*(n+1) for i in range(m+1)]

# 	for i in range(1,m+1):
# 		for j in range(1,n+1):
# 			if x[i-1] == y[j-1]:
# 				c[i][j] = c[i-1][j-1] + 1
# 			elif c[i-1][j] >= c[i][j-1]:
# 				c[i][j] = c[i-1][j]
# 			else:
# 				c[i][j] = c[i][j-1]
# 	return c

x = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
y = ['B', 'D', 'C', 'A', 'B', 'A']

x1 = ['A', 'C', 'C', 'G', 'G', 'T', 'C', 'G', 'A', 'G', 'T', 'G', 'C', 'G', 'C', 'G', 'G', 'A', 'A', 'G', 'C', 'C', 'G', 'G', 'C', 'C', 'G', 'A', 'A']
y1 = ['G', 'T', 'C', 'G', 'T', 'T', 'C', 'G', 'G', 'A', 'A', 'T', 'G', 'C', 'C', 'G', 'T', 'T', 'G', 'C', 'T', 'C', 'T', 'G', 'T', 'A', 'A', 'A']
answer, print_answer = lcs_length(x1, y1)
#print(answer)
print(answer[len(x1)][len(y1)])
print_lcs(print_answer, x1, len(x1), len(y1))
print()
#print(print_answer)
#print()

answer, print_answer = lcs_length(x, y)
#print(answer)
print(answer[len(x)][len(y)])
print_lcs(print_answer, x, len(x), len(y))

print()

#print(print_answer)

