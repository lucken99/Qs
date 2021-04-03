# Meetings
import sys
input = sys.stdin.readline

# def twelve2twenty4(p):
# 	h, m = p[0].split(':')
# 	if p[1] == 'PM' and h != '12':
# 		h  = str(int(h)+12)
# 	elif p[1] == 'AM' and h == '12':
# 		h = '00'
# 	t = int(str(h)+str(m))
# 	return t

# for _ in range(int(input())):
# 	p = input().split()
# 	t = twelve2twenty4(p)
# 	# print(t)
# 	n = int(input())
# 	for i in range(n):
# 		time = input().split()
# 		t1 = twelve2twenty4(list([time[0]]+ [time[1]]))

# 		t2 = twelve2twenty4(list([time[2]]+[time[3]]))


# 		if t1 <= t and  t <= t2:
# 			print(1, end="")
# 		else:
# 			print(0, end="")
# 		# print('\n'+str(t1), t2)

# 	print()



# import math
# for _ in range(int(input())):
# 	n = int(input())
# 	w = list(map(int, input().split()))
# 	l = list(map(int, input().split()))
# 	d = dict(zip(w, l))
# 	# print(d)
# 	ans = 0

# 	p = [[w[i], i+1] for i in range(n)]
# 	p.sort()
# 	# print(p)

# 	for i in range(1, n):
# 		if p[i][1] <= p[i-1][1]:
# 			z = p[i-1][1] - p[i][1] + 1
# 			if d[i+1] >= z:
# 				ans += 1
# 				p[i][1] += d[i+1]
# 			else:
# 				ans += math.ceil(z/d[i+1])
# 				p[i][1] += math.ceil(z/d[i+1])*d[i+1]
# 	print(ans)


# Team Name
# from collections import defaultdict
# for _ in range(int(input())):
# 	n = int(input())
# 	w = input().split()
# 	ans = 0
# 	s = set(w)
# 	# brute force
# 	# for i in range(n):
# 	# 	for j in range(i+1, n):
# 	# 		if (w[i][0]+w[j][1:] not in s) and (w[j][0]+w[i][1:] not in s):
# 	# 			ans += 2

# 	# using defaultdict
# 	d = defaultdict(list)
# 	for word in w:
# 		d[word[1:]].append(word[0])
# 	print(d)
# 	listd = list(d.keys())
# 	for i in range(len(d)):
# 		for j in range(i+1, len(d)):
# 			z = len(set(d[listd[i]] + d[listd[j]]))
# 			ans += (z-len(d[listd[i]])) * (z - len(d[listd[j]]))
# 	print(ans*2) 


# XOR Sum
# import sys
# input = sys.stdin.readline
# n = int(input())
# a = list(map(int, input().split()))


# q = int(input())
# for i in range(q):
# 	l = int(input())