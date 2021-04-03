def suml(a):
	sum = 0
	for i in range(len(a)-1):
		sum += abs(int(a[i]) - int(a[i+1]))
	return sum


for i in range(int(input())):
	n, q = map(int, input().split())
	#a = list(map(int, input().split()))
	a = input()
	a = a.replace(' ','')

	ans = []
	for i in range(q):
		x, y = map(int, input().split())
		a = a.replace('x', 'y')
		ans.append(suml(a))
	for j in range(len(ans)):
		print(ans[j])



