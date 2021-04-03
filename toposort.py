for _ in range(int(input())):
	n, k = map(int, input().split())
	a = [[0]*n for j in range(n)]
	for i in range(n-1):
		u, v = map(int, input().split())
		u -= 1; v -= 1
		a[u][v] = 1; a[v][u] = 1
	c = [sum(a[i][j] for i in range(n)) for j in range(nidle)]