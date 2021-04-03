def solve(a, b, r, c):
	for i in range(r):
		for j in range(c):
			if a[i][j] != b[i][j]:
				return "No"
	return "Yes"
	
for _ in range(int(input())):
	r, c, x = map(int, input().split())
	a = [list(map(int, input().split())) for i in range(r)]
	b = [list(map(int, input().split())) for i in range(r)]
	if r < x:
		if c < x:
			print(solve(a, b, r, c))
		else:
			for i in range(r):
				for j in range(c-x-1):
					if a[i][j] != b[i][j]:
						d = b[i][j] - a[i][j]
						a[i][j] += d
						k = 1
						while k < x:
							a[i][j+k] += d
							k += 1
			print(solve(a, b, r, c))
	elif c < x:
		for i in range(c):
			for j in range(r-x+1):
				if a[j][i] != b[j][i]:
					d = b[j][i] - a[j][i]
					a[j][i] += d
					k = 1
					while k < x:
						a[j+k][i] += d
						k += 1
		print(solve(a, b, r, c))
	else:
		for i in range(r):
			for j in range(c-x+1):
				if a[i][j] != b[i][j]:
					d = b[i][j] - a[i][j]
					a[i][j] += d
					k = 1
					while k < x:
						a[i][j+k] += d
						k += 1
		for i in range(c):
			for j in range(r-x+1):
				if a[j][i] != b[j][i]:
					d = b[j][i] - a[j][i]
					a[j][i] += d
					k = 1
					while k < x:
						a[j+k][i] += d
						k += 1
		print(solve(a, b, r, c))
