for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()
    count = 0
    minimum = sum(a[:k+1])
    temp = 0
    for i in range(k+1):
        for j in range(i, k+1+i):
            temp += a[j]
        if temp == minimum:
            count += 1
            temp = 0
        else:
            break
    print(count)