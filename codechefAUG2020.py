# for i in range(int(input())):
# 	h, p = map(int, input().split())
# 	ans = 1
# 	while True:
# 		h -= p
# 		p = p//2
# 		if p == 0 and h > 0:
# 			ans = 0
# 			break
# 		elif p>=0 and h <=0:
# 			ans = 1
# 			break
# 	print(ans)


# for i in range(int(input())):
# 	n, k = map(int, input().split())
# 	p = list(map(int, input().split()))
# 	min = [10**10,10**10]
# 	for i in range(len(p)):
# 		if (k%p[i] == 0):
# 			if k//p[i] < min[0]:
# 				min[0] = k//p[i]
# 				min[1] = p[i]
# 		elif i == (len(p)-1) and (min[1] == 10**10):
# 			min[1]  = -1
# 	print(min[1])
# 	


# from math import ceil
# for i in range(int(input())):
# 	pc, pr = map(int, input().split())
# 	winner = 1
# 	no_digits = 0
# 	if (ceil(pc/9) >= ceil(pr/9)):
# 		winner = 1
# 		no_digits = ceil(pr/9)
# 	else:
# 		winner = 0
# 		no_digits = ceil(pc/9)
# 	print(winner, no_digits)



# for i in range(int(input())):
# 	s = input()
# 	p = input()
# 	for i in p:
# 		s = s.replace(i,'',1)
# 	d = sorted(s)
# 	ind = 0
# 	for i in range(len(d)):
# 		if d[i] > p[0]:
# 			ind = i
# 			break
# 		elif d[i] == p[0]:
# 			j = 0
# 			while d[i] == p[j]:
# 				j += 1
# 			if d[i] > p[j]:
# 				ind = i 
# 				break
# 		elif i == (len(d) - 1) and (ind == 0):
# 			ind = len(d)
# 	d.insert(ind,p)
# 	d = ''.join(d)

# 	print(d)


# from collections import Counter
# for i in range(int(input())):
# 	n, k = map(int, input().split())
# 	f = list(map(int, input().split()))
	
# 	if k ==1:
# 		sums = 0
# 		ct = Counter(f)
# 		for i in ct:
# 			if ct[i] > 1:
# 				sums += ct[i]

# 		print(min( k*(ct.most_common(1)[0][1]), k+sums ))




# 	arg = 0
# for i in range(len(f)):
# 	if f.count(f[i]) > 1:
# 		arg = f.count(f[i])
# 		break
# if k*arg <= k+arg:
# 	print(k*arg)
# else:
# 	print(k+arg)


from collections import OrderedDict
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = sorted(a)
    d = OrderedDict()
    for i in range(len(s)):
        sums = (len(s[i+1:])*(  len(s[i+1:])  + 1 ))//2
        d[s[i]]  = 1 + sums

    for i in range(1,n+1):
        try:
            print(d[i])
        except:
            print(0)