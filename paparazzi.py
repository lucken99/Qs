import sys
input = sys.stdin.readline

for _ in range(int(input())):
	n = int(input())
	h = list(map(int, input().split()))
	a = [(i+1, h[i]) for i in range(n)]

	if n == 2:
		print(1)
	else:
		st = [a[0], a[1]]
		ans = 1
		l = 2
		for i in range(2, n):
			while len(st) >= 2:
				m1 = (st[l-1][1] - st[l-2][1])/(st[l-1][0] - st[l-2][0])
				m2 = (a[i][1] - st[l-1][1]) / (a[i][0] - st[l-1][0])
				if m1 <= m2:
					st.pop()
					l -= 1
				else:
					break
			st.append(a[i])
			l += 1
			ans = max(ans, st[l-1][0] - st[l-2][0])
		print(ans) 