t = int(input())
while t:
	t -= 1
	n = int(input())
	l = input().split()
	s = input()
	a = []
	cs = ''
	ans = 1

	d = {l[i] : i for i in range(len(l))}
	i = 0
	while i < len(s):
		if cs in d:
			a.append(cs)
			cs = ''
		else:
			cs += s[i]
			i += 1
	a.append(cs)
	for i in a:
		if i not in d:
			ans = 0
			break
	print(ans)



//wrong code not pass all test cases
//but pass easy one

