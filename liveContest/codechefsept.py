# for _ in range(int(input())):
# 	n = int(input())
# 	v = list(map(int, input().split()))

# 	# best = 1
# 	# worst = 1
# 	# for i in range(1, n):
# 	# 	if v[i] <= v[i-1] and v[i-1] != 0:
# 	# 		best += 1
# 	# 	else:
# 	# 		break
# 	# for i in range(n-1):
# 	# 	if v[i] >= v[i+1] and v[i] != 0:
# 	# 		worst += 1

# 	if v.index(max(v)) == 0:
# 		best, worst = n, n
# 	elif v.index(min(v)) == 0:
# 		best = 1
# 		worst = len(v[v.index(max(v)) : ])

# 	print(best, worst)

# for _ in range(int(input())):
# 	n = int(input())
# 	a = []
# 	ans = 0
# 	for i in range(n):
# 		a.append(list(map(int, input().split())))
# 	for i in reversed(range(1,n)):
# 		if a[i][0] != (i*n)+1:
# 			ans += 1
# 		elif ans != 0:
# 			if ans%2==0:
# 				if a[i][0] != (i*n)+1:
# 					ans += 1
# 			else:
# 				if a[i][0] == i*n+1:
# 					ans += 1
# 	print(ans)

# for _ in range(int(input())):
# 	n = int(input())
# 	a = []
# 	for i in range(n):
# 		a.append(list(map(int, input().split())))
# 	flag = True
# 	count = 0
# 	for i in reversed(range(1, n)):
# 		if a[i][0] != (i*n)+1 and flag:
# 			count += 1
# 			flag = False
# 		elif a[i][0] == (i*n)+1 and not flag:
# 			count += 1
# 			flag = True
# 	print(count)
# 	b = []
# 	ans = 0
# 	for i in reversed(range(1, n)):
# 		if a[i][0] != (i*n)+1:
# 			b.append(False)
# 		else:
# 			b.append(True)
# 	print(b)
# 	for i in range(len(b)):
# 		if b[i] == False:
# 			ans += 1
# 			for j in range(i,len(b)):
# 				if b[j] == True:
# 					b[j] = False
# 				else:
# 					b[j] = True
# 			print(b)
# 	#print(b)
# 	print(ans)
			




# chefina and swap
# def squareSum(N):  
  
#     Sum = (N  * (N + 1)) // 2
#     return Sum 
# # print(squareSum(83)+squareSum(34))
# def findMaxN(X): 
  
#     low, high, N = 1, 1000000000, 0
  
#     while low <= high: 
#         mid = (high + low) // 2
  
#         if squareSum(mid) <= X:  
#             N = mid  
#             low = mid + 1
          
#         else: 
#             high = mid - 1
      
#     return N
# # print(findMaxN(250000000250000000))
# # print(findMaxN(squareSum(119)//2))
# # print(findMaxN(squareSum(24)//2))
# # print(findMaxN(3))
# # print(squareSum(84) == 3570)
# for _ in range(int(input())):
# 	n = int(input())

# 	sums = squareSum(n)
# 	if n == 3:
# 		print(2)
# 	elif sums%2 != 0:
# 		print(0)
# 	else:
# 		half = sums//2
# 		check = 0
# 		ans = 0
# 		check = findMaxN(half)
# 		if squareSum(check) < half:
# 			ans = n-check
# 		elif squareSum(check) == half:
# 			ans = squareSum(check-1) + squareSum(n-check-1) + n-check
# 			# print(n)
# 			#print("yes", end="")
# 		print(ans)

# COVID19B
# for _ in range(int(input())):
#     n = int(input())
#     v = list(map(int, input().split()))
#     a = [[] for i in range(0, 6)]
#     for i in range(n):
#         ma = v[i]
#         for j in range(n):
#             if j < i:
#                 if v[i] < v[j]:
#                     a[i] += [j]
#                     ma = max(ma, v[j])

#             elif j > i:
#                 if ma > v[j]:
#                     a[i] += [j]
#             else:
#                 a[i] += [j]
    
#     #print(list(set(i) for i in a if len(i) != 0))
#     mini = float('inf')
#     maxi = float('-inf')
#     for i in a:
#         if len(i) != 0:
#             mini = min(mini, len(set(i)))
#             maxi = max(maxi, len(set(i)))
#     print(mini, maxi)
#     #a = list(set(i) for i in a)
#     #print(a)
    
# COVID19B

def time(i1, i2):
    try:
        return (i2-i1) / (v[i1] - v[i2])
    except:
        return -1
for _ in range(int(input())):
    n = int(input())
    v = list(map(int, input().split()))
    a = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                a[i][j] = time(i,j)
            else:
                a[i][j] = 0
                
    print(a)



		




# # Divide candles
# k = int(input())
# for _ in range(int(input())):
# 	n = int(input())
# 	ans = []
# 	if k == 1:
# 		for i in range(n):
# 			if i%2 != 0:
# 				ans.append(1)



	






