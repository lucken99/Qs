def slide(s, size, no, nz, l, so, se, n):
	sew = set()
	sew.add(tuple(((no, nz), (so, se))))
	for i in range(size, n):
		if s[i-size] == '1':
			l.remove(l[0])
			se, so = so, se
			no -= 1

		else:
			nz -= 1
			l[0] -= 1
			se -= 1


		if s[i] == '1':
			no += 1
			l.append(0)
		else:
			nz += 1
			l[len(l)-1] += 1
			if len(l)%2 == 1:
				se += 1
			else:
				so += 1
		sew.add(tuple(((no, nz), (so, se))))
	return len(sew)

l = []
# print(slide('101010111', 10, 0, 5, l, 10, 25 ,5))

for _ in range(int(input())):
	s = input()
	n = len(s)
	no = s.count('1')
	nz = s.count('0')

