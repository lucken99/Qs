# from itertools import product
# def sum_of_tup(n):
#     sum=0
#     for i in range(len(n)):
#         sum=sum+int(n[i])
#     return sum
# low,high=map(int,input().split())
# k=int(input())
# lst=[]
# for i in range(low,high+1):
#     lst.append(str(i))
# count=0
# perm=product(lst,repeat=k)
# for i in perm:
#     if (sum_of_tup(i)%2==0):
#         count+=1
# print(count%1000000007)



def countOdd(l, h):
		n = (h-l) // 2

		if (h%2 !=0) or (l%2 !=0):
			n += 1
		return n


for _ in range(int(input())):
	l, h = map(int, input().split())
	odds = countOdd(l, h)
	even = (h-l+1) - odds
	k = int(input())
	a = []
	if k == 0:
		print(1)
	elif even-odds == 0:
		a.append(even)
		for i in range(1,k):
			a.append(a[i-1]*(even+odds))
		print(a[k-1])
	elif even-odds == 1:
		a.append(even)
		for i in range(1,k):
			a.append(a[i-1]*(even+odds)-1)
		print(a[k-1])
	elif odds-even == 1:
		a.append(l)
		for i in range(1,k):
			if i%2 == 0:
				a.append(a[i-1]*k+2)
			else:
				a.append(a[i-1]*k-2)
	elif (even-odds == 2) and (even%2==0):
		print(1)
	else:
		if k%2==0:
			print(1)
		else:
			print(0)



