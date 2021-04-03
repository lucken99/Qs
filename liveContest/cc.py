# Arange the dates
# n = int(input())
# a = []
# for _ in range(n):
# 	a.append(input())
# a.sort(key=lambda x:int(x[:x.index('/')]) + int(x[x.index('/')+1:x.index('/', 3)]) * 30 + int(x[x.index('/', 3)+1:])*365)
# for i in a:
# 	print(i)

# largest sum consecutive increasing digit in a number
# a=input()
# ans=[]
# for i in range(len(a)):
#     sum=int(a[i])
#     m=0
#     for j in range(i,len(a)-1):
#         if a[j+1]>a[j]:
#             sum=sum+int(a[j+1])
#             m+=1
#         else:
#             break
#     ans.append([sum, i+1, i+m+1]) 
# #print(ans)

# p = max(ans)
# print(str(p[0])+':'+str(p[1])+'-'+str(p[2]))

# prime
# a = int(input())
# b = int(input())

# ans = []
# l = a/2 * b/2
# r = a*b
# for num in range(a,b+1):  
#    if num > 1:  
#        for i in range(2,num):  
#            if (num % i) == 0:  
#                break  
#        else:  
#            ans.append(num)
# #print(ans)

# for i in range(len(ans)):
# 	for j in range(i+1, len(ans)):
# 		if ans[i]*ans[j] <= r and ans[i]*ans[j] >= l:
# 			print(str(ans[i]) + ',' + str(ans[j]))

# reverse
# n = input()
# l = len(n)
# def ans(n, l):
# 	for i in range(1,l+1):
# 		if int(n[:i+1]) % (l-i+1) != 0:
# 			return "No"

# 	return "Yes"
# print(ans(n, l))

# pattern

# for _ in range(int(input())):
# 	s = ['S', 'SS', 'SSE', 'SSEC', 'SSE', 'SS', 'S']
# 	n = int(input())
# 	ans = []
# 	for i in s[n%7-1]:
# 		ans.append(ord(i))
# 	print(" ".join(str(k) for k in ans))

# for _ in range(int(input())):
# 	n = input()
# 	a = []
# 	for i in range(len(n)):
# 		a.append(str(int(n[i])-2))
# 	print("".join(a))

#Just find it
from collections import defaultdict
for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	sums = 0
	even = 0
	odd  = 0
	d = defaultdict(int)
	s = set()
	




