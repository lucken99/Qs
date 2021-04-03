# for _ in range(int(input())):
#   n = int(input())
#   a = list(map(int, input().split()))
#   ans = 0
#   for i in range(n-1):
#       for j in range(i+1, n):
#           if a[i] & a[j] == a[i]:
#               ans += 1
#   print(ans)

# for _ in range(int(input())):
#   s = list(input().split())
#   x1, y1 = map(int, input().split())
#   q = int(input())
#   seqr = 0
#   seql = 0
#   sequ  = 0
#   seqd = 0
#   for i in range(q):
#       x2, y2 = map(int, input())
#       if (x1==x2) and (y1==y2):
#           print("YES", 0)

# n, m = map(int,input().split())
# a= []

# for i in range(n):
#     a.append(list(input()))

# q = int(input())

# for i in range(q):
#     x1, y1, x2, y2 = map(int, input().split())

#     for i in range(x1-1,x2):
#         for j in range(y1-1, y2):
#             a[i][j] = '0' if a[i][j] == '1' else '1'
# print('\n'.join(map(''.join, a)))

#correct solution CENS20A
# import sys
# n,m=map(int,input().split())
# dp=[[0 for j in range(m+2)] for k in range(n+2)]
# a=[]
# for j in range(n):
#     t=sys.stdin.readline().strip()
#     a.append(list(t))
# q=int(input())
# for j in range(0,q):
#     x1,y1,x2,y2=map(int,sys.stdin.readline().split())
#     dp[x1][y1]+=1
#     dp[x2+1][y2+1]+=1
#     dp[x1][y2+1]-=1
#     dp[x2+1][y1]-=1
# #print(dp)
# for j in range(1,n+1):
#     for k in range(1,m+1):
#         dp[j][k]=dp[j][k]+dp[j-1][k]+dp[j][k-1]-dp[j-1][k-1]
#         #print(dp[j][k],a[j-1][k-1])
#         if dp[j][k]%2!=0:
#             a[j-1][k-1]=int(a[j-1][k-1])^1
# for j in range(n):
#     print(''.join(map(str,a[j])))


#CENS20G Martha
# from sys import stdin, stdout

# I = stdin.readline
# print=stdout.write
# for _ in range(int(I())):
#     li = list(I())
#     x1, y1 = map(int, I().split())
#     q = int(I())
#     di = dict()
#     for i in li:
#         if i in di:
#             di[i] += 1
#         else:
#             di[i] = 1

#     for i in range(q):
#         a, b = map(int, I().split())
#         xx = False
#         yy = False
#         ans = 0
#         t = x1 - a
#         if t==0:
#             xx=True
#         if a < x1:
#             if 'L' in di and di['L'] >= abs(t):
#                 xx = True
#                 ans += abs(t)
#         if a > x1:
#             if 'R' in di and di['R'] >= abs(t):
#                 xx = True
#                 ans += abs(t)
#         t1=y1-b
#         if t1==0:
#             yy=True
#         if b < y1:
#             if 'D' in di and di['D'] >= abs(t1):
#                 yy = True
#                 ans += abs(t1)
#         if b > y1:
#             if 'U' in di and di['U'] >= abs(t1):
#                 yy = True
#                 ans += abs(t1)
#         if xx and yy:
#             print('YES'+' '+str(ans)+'\n')
#         else:
#             print('NO'+'\n')



s = input()
t = input()
sl = len(s)
tl = len(t)
q = int(input())
ans = 0
for _ in range(q):
    n = int(input())
    if (n >= tl) and ( t in s*(n//sl)+s[:(n%sl)]):
        s = s*(n//sl)+s[:(n%sl)]
        ans = s.count(t)
    print(ans)



        








