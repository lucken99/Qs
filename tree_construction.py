n, b = map(int, input().split())
if b > (n*(n+1))//2:
    print(-1)
elif b < 2*n-1:
    print(-1)
elif b == (n*(n+1))//2:
    for i in range(n-1):
        print(i+1, i+2)
elif b == 2*n-1:
    for i in range(1, n):
        print(1, i+1)
elif n >= 2:
    s = (n*(n+1))//2
    ans = [[i, i+1] for i in range(1, n)]
    # print(ans)
    act_s = s - b
    i = 0
    k = 1
    while i < act_s:
        l = -1
        for j in range(k):
            if i == act_s:
                break
            ans[l][0] -= 1
            l -= 1
            i += 1
        k += 1
    for i, j in ans:
        print(i, j)
    # print(ans)