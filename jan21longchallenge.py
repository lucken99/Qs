# # Fair Elections
# # https://www.codechef.com/JAN21B/problems/FAIRELCT
# for _ in range(int(input())):
#   n, m = map(int, input().split())
#   a = list(map(int, input().split()))
#   b = list(map(int, input().split()))

#   sa = sum(a)
#   sb = sum(b)
#   swaps = 0
#   a.sort(reverse=True)
#   b.sort()
#   flag = True
#   i = -1
#   while i >= -min(n, m):
#       if sa > sb:
#           break
#       else:
#           sa += b[i]
#           sa -= a[i]
#           sb += a[i]
#           sb -= b[i]
#           swaps += 1
#           i -= 1
#   if sa > sb:
#       print(swaps)
#   else:
#       print(-1)


# Watching CPL
# https://www.codechef.com/JAN21B/problems/WIPL

# def isSubsetSum(set, n, sum):
    
#     # The value of subset[i][j] will be 
#     # true if there is a
#     # subset of set[0..j-1] with sum equal to i
#     subset =([[False for i in range(sum + 1)] 
#             for i in range(n + 1)])
    
#     # If sum is 0, then answer is true 
#     for i in range(n + 1):
#         subset[i][0] = True
        
#     # If sum is not 0 and set is empty, 
#     # then answer is false 
#     # for i in range(1, sum + 1):
#     #   subset[0][i]= False
            
#     # Fill the subset table in botton up manner
#     for i in range(1, n + 1):
#         for j in range(1, sum + 1):
#             if j<set[i-1]:
#                 subset[i][j] = subset[i-1][j]
#                 # subset[i][j] = True
#             elif j>= set[i-1]:
#                 subset[i][j] = (subset[i-1][j] or
#                                 subset[i - 1][j-set[i-1]])
    
#     # uncomment this code to print table 
#     # for i in range(n + 1):
#     #     for j in range(sum + 1):
#     #         print (subset[i][j], end =" ")
#     #     print()
#     return subset[n][sum]


# for _ in range(int(input())):
#     n, k = map(int, input().split())
#     h = list(map(int, input().split()))
#     h.sort(reverse=True)
#     # print(h)
#     hs = sum(h)
#     if hs < 2*k:
#         print(-1)
#     else:
#         ans = 0
#         s = 0
#         z = []
#         i = 0
#         while s < 2*k:
#             z.append(h[i])
#             s += h[i]
#             i += 1
#         if isSubsetSum(z,i,k):
#             print(i)
#         else:
#             s = 0
#             ans = 0
#             for i in range(n):
#                 s += h[i]
#                 ans += 1
#                 if s >= k:
#                     break
#             # print(i)

#             if s == k:
#                 s = 0
#                 for j in range(i+1, n):
#                     s += h[j]
#                     ans += 1
#                     if s >= k:
#                         break
#                 print(ans)
#             else:
#                 s -= h[i]
#                 ans = i
#                 f = 0
#                 for j in range(n-1, ans-1, -1):
#                     if s + h[j] >= k:
#                         s += h[j]
#                         ans += 1
#                         f = j
#                         break
#                 s = 0
#                 for j in range(i, n):
#                     if j != f:
#                         s += h[j]
#                         ans += 1
#                         if s >= k:
#                             break
                        
#                 if s >= k:
#                     print(ans)
#                 else:
#                     print(-1)










    


# Chef and Ants

# subtask 30
for _ in range(int(input())):
    n = int(input())
    x = [list(map(int, input().split())) for i in range(n)]
    s = set()
    for i in range(n):
        for j in range(1, x[i][0]+1):
            s.add(x[i][j])
    neg = 0
    pos = 0
    for i in s:
        if i < 0:
            neg += 1
        else:
            pos += 1
    print(neg*pos)
        



# And-or-Game

# for _ in range(int(input())):
#     n, m = map(int, input().split())
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))

    
# for _ in range(int(input())):
#     n = int(input())
#     x = [list(map(int, input().split())) for i in range(n)]
#     s = set()
#     ans = 0
#     for i in range(n):
#         neg = 0
#         pos = 0
#         for j in range(1, x[i][0]+1):
#             if x[i][j] < 0:
#                 neg += 1
#             else:
#                 pos += 1
#         ans += (neg*pos)
#     print(ans)

# blackjack
for _ in range(int(input())):
    n, x, y = map(int, input().split())
    for i in range(n):
        a = list(map(int, input().split()))
        # a.sort()
        sa = 0
        swaps = 0
        for i in range(n):
            sa += a[i]
            if sa in range(x, y+1):
                print(swaps)
                break
            elif sa > y:
                sa -= a[i]
                for j in range(i, n):
                    if sa + a[j] in range(x, y+1):
                        

        
