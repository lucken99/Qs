# n = int(input())
# a = list(map(int, input().split()))
# q = int(input())
# # for i in range(q):
# #     query = list(map(int, input().split()))
# #     if query[0] == 3:
# #         try:
# #             l = a.index(query[1])
# #             r = (n-1) - a[::-1].index(query[1])
# #             print(r-l+1)
# #         except:
# #             print(-1)
        

# #     elif query[0] == 1:
# #         for i in range(query[1]-1, query[2]):
# #             a[i] += query[-1]
# #     elif query[0] == 2:
# #         for i in range(query[1]-1, query[2]):
# #             a[i] *= query[-1]

t = int(input())
while t:
    t -= 1
    l, r, k = map(int, input().split())
    if k>4:
        rlen = len(r)
        
