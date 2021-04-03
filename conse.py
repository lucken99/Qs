def ans(a, b, r, c):
	for i in range(r):
		for j in range(c):
			if a[i][j] != b[i][j]:
				return False
	return True


if __name__ == '__main__':
	for _ in range(int(input())):
		r, c, x = map(int, input().split())
		a = [list(map(int, input().split())) for i in range(r)]
		b = [list(map(int, input().split())) for i in range(r)]
		if r < x and c < x:
			if ans(a, b, r, c):
				print("Yes")
			else:
				print("No")
		elif r < x:
			for i in range(r):
				for j in range(c-x-1):
					if a[i][j] != b[i][j]:
						diff = b[i][j] - a[i][j]
						a[i][j] += diff
						k = 1
						while k < x:
							a[i][j+k] += diff
							k += 1
			if ans(a, b, r, c):
				print("Yes")
			else:
				print("No")
		elif c < x:
			for i in range(c):
				for j in range(r-x+1):
					if a[j][i] != b[j][i]:
						diff = b[j][i] - a[j][i]
						a[j][i] += diff
						k = 1
						while k < x:
							a[j+k][i] += diff
							k += 1
			if ans(a, b, r, c):
				print("Yes")
			else:
				print("No")
		elif c >= x and r >= x:
			for i in range(r):
				for j in range(c-x+1):
					if a[i][j] != b[i][j]:
						diff = b[i][j] - a[i][j]
						a[i][j] += diff
						k = 1
						while k < x:
							a[i][j+k] += diff
							k += 1
			for i in range(c):
				for j in range(r-x+1):
					if a[j][i] != b[j][i]:
						diff = b[j][i] - a[j][i]
						a[j][i] += diff
						k = 1
						while k < x:
							a[j+k][i] += diff
							k += 1
			if ans(a,b,r,c):
				print("Yes")
			else:
				print("No")
