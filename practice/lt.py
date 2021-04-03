# from collections import Counter
# for i in range(int(input())):
# 	n = int(input())
# 	a = list(map(int, input().split()))

# 	c = Counter(a)
# 	f = []
# 	for i in c.keys():
# 		f.append(c[i])
# 	f.sort()
# 	c = Counter(f)
# 	print(c.most_common(1)[0][0])

# def getMaxLength(arr, n): 
  
     
#     count = 0 
      
    
#     result = 0 
  
#     for i in range(0, n): 
      
       
#         if (arr[i] == 1): 
#             count = 0
  
        
#         else: 
              
            
#             count+= 1 
#             result = max(result, count)  
          
#     return result

# for i in range(int(input())):
# 	n = int(input())
# 	a = list(map(int, input().split()))

# 	c = getMaxLength(a, n)
# 	#print(c)
# 	if c%2 == 0:
# 		print("No")
# 	elif (c == 1) and (a.count(0)%2==0):
# 		print("No")
# 	else:
# 		print("Yes")

for _ in range(int(input())):
	n, m = map(int, input().split())
	r = list(map(int, input().split()))
	ans = 0
	a = []
	# for i in range(n):
	# 	a.append(list(map(lambda x:r[i]+int(x), input().split())))
	# for i in range(n):
	# 	count = 0
	# 	for j in range(1,m):
	# 		if a[i][j-1] < a[i][j]:
	# 			count += 1
	# 	if a[i].index(max(a[i])) == count:
	# 		ans += 1

	for i in range(n):
		for j in range(m):
			a.append(list(map(int, input().split())))
	


	print(ans)

	#print(a)
