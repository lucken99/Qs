# for _ in range(int(input())):
#   n = int(input())
#   s = input()
#   p = input()
#   if (s.count('1') == p.count('1')) and (s.count('0') == p.count('0')) and (n-(s[::-1].index('1'))-1 <= p.index('1')):
#       print("Yes")
#   else:
#       print("No")




# from collections import Counter
# for _ in range(int(input())):
# 	s = input()
# 	c = Counter(s)
# 	if max(c.values()) == 1:
# 		print(0)
		
# 	else:
# 		s = sum(i for i in c.values())
# 		print(s//3)

# for _ in range(int(input())):
# 	s = input()
# 	freq = [0]*26
# 	for i in s:
# 		freq[ord(i)-ord('a')] += 1
# 	c, c1, c2 = 0, 0, 0
# 	for i in range(26):
# 		if freq[i]:
# 			c2 += freq[i]//2

# 			if freq[i]&1:
# 				c1 += 1
# 	if c1 == c2:
# 		c = c1
# 	elif c1 > c2:
# 		c = c2
# 	elif c2 > c1:
# 		c = c1 + ((c2-c1)*2)//3
# 	print(c)



	


# for _ in range(int(input())):
# 	n = int(input())
# 	s = input()
# 	p = input()
# 	so = s.count('1')
# 	po = p.count('1')
# 	s1 = []
# 	p1 = []
# 	for i in range(n):
# 		if s[i] == '1':
# 			s1.append(i)
# 		if p[i] == '1':
# 			p1.append(i)
# 	b = True
# 	if (so == po) and (s.count('0') == p.count('0')):
# 		for i in range(len(s1)):
# 			if s1[i] > p1[i]:
# 				print("No")
# 				b = False
# 				break
# 		if b:
# 			print("Yes")

	
# 	else:
# 		print("No")