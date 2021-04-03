


# for _ in range(int(input())):
# 	n, k = map(int, input().split())
# 	a = list(map(int, input().split()))

# 	d = dict((i,0) for i,j in enumerate(a))
# 	ans = float('inf')


# 	col = [[0]*(n+1) for i in range(n+1)]

# 	for i in range(n):
# 		for j in range(i, n):
# 			col[i][j] = 0 if j==0 else col[i][j-1]
# 			if a[j] in d.keys():
# 				if d[a[j]] == 1:
# 					col[i][j] += 1
# 				col[i][j] += 1
# 			if d[a[j]] not in d.keys():
#                d[a[j]] = 0


				


# 	print(d)
# 	print(col)
# 	table = 100
# 	dp = [[0]*1001 for i in range(101)]

# 	for i in range(n+1):
# 		dp[1][i] = col[0][i-1]

# 	for i in range(2, table+1):
# 		dp[i][1] = 0
# 	for i in range(2, table+1):
# 		for j in range(2, n+1):
# 			best = float("inf")
# 			for p in range(1, j):
# 				best = min(best, dp[i-1][p] + col[p][j-1]);

# 			dp[i][j] = best

# 	for table in range(1, 101):
# 		ans = min(table*k+dp[table][n], ans)
# 	print(ans)



# t=int(input())
# while t>0:
#     t-=1
#     n,k=list(map(int,input().split()))
#     guests=list(map(int,input().split()))
#     MLimit=0
#     mx=9999999999
#     res=0
#     #cont=[]
#     ans1=mx
#     while(True):
#         cnl=[]
#         dic={}
#         totCost=0
#         cost=0
#         Lim=MLimit
#         for i in guests:
#             if((i in dic) and (Lim != 0) ):
#                 Lim-=1
#                 if(dic[i] == 0):
#                     dic[i]=1
#                     cost+=2
#                 else:
#                     cost+=1
#             elif(i in dic) and (Lim == 0):
#                 cnl.append(dic)
#                 dic={}
#                 dic[i]=0
#                 totCost+=cost
#                 cost=0
#                 Lim=MLimit
#             else:
#                 dic[i]=0
#         cnl.append(dic) 
#         totCost+=cost
#         ans1=min(ans1,len(cnl)*k + totCost)
#         #print(totCost,cnl,ans1)
#         #print(dic)
#         MLimit+=1
#         if(len(cnl) == 1):
#             break
#     MLimit=0
#     ans2=mx
#     guests.reverse()
#     #for reversed case
#     while(True):
#         cnl=[]
#         dic={}
#         totCost=0
#         cost=0
#         Lim=MLimit
#         for i in guests:
#             if((i in dic) and (Lim != 0) ):
#                 Lim-=1
#                 if(dic[i] == 0):
#                     dic[i]=1
#                     cost+=2
#                 else:
#                     cost+=1
#             elif(i in dic) and (Lim == 0):
#                 cnl.append(dic)
#                 dic={}
#                 dic[i]=0
#                 totCost+=cost
#                 cost=0
#                 Lim=MLimit
#             else:
#                 dic[i]=0
#         cnl.append(dic) 
#         totCost+=cost
#         ans2=min(ans2,len(cnl)*k + totCost)
#         MLimit+=1
#         if(len(cnl) == 1):
#             break
#     res=min(ans1,ans2)
#     print(res)





#2nd sol

from collections import Counter
def solve():
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    i=0
    ans1=float('inf')
    while(i<=n):
        x,y=0,0
        d=Counter(l[:i])
        d1=Counter(l[i:])
        for j in d:
            if (d[j]>1):
                x+=d[j]
        for j in d1:
            if (d1[j]>1):
                y+=d1[j]
        if (i==0):
            c=k+y
        elif (i==n):
            c=k+x
        else:
            c=2*k+x+y
 
        ans1=min(c,ans1)
        i+=1

        

    a=set()
    p=1
    for i in l:
        if i in a:
            a={i}
            p+=1
        else:
            a.add(i)
        
    ans2=p*k
       
    ans=min(ans1,ans2)
    print(ans)

for _ in range(int(input())):
        solve()