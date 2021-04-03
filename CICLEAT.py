# for _ in range(int(input())):
# 	n = int(input())
# 	a = list(map(int, input().split()))


a = [4, 15, 20, 3]
n = len(a)
pref = [0]*n
pref[1:] = [pref[i-1] + a[i] for i in range(1, n)]

suf = [0]*(n+1)
for i in range(n-1, 0, -1):
	suf[i] = suf[i+1] + a[i]
print(pref)
print(suf)

low = 0
high = int(1e18)
while low < high:
	mid = (low + high) >> 1
	l = 0
	r = n
	mp = 0
	ms = 0

	while l+1 < r:
		changed = False
		while l+1 < r and pref[l+1] + ms >= -mid:
			mp = max(mp, pref[l+1])
			changed = True
			l += 1
		while l+1 < r and suf[r-1] + mp >= -mid:
			ms = max(ms, suf[r-1])
			changed = True
			r -= 1
		if not changed:
			break
	if l+1 >= r:
		high = mid
	else:
		low = mid + 1

print(min(a[0] - low, a[0] + pref[n-1]))


