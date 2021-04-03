def xorfft(a):
    a = list(a)
    la = len(a)
    assert la & (la-1) == 0
    k = 1
    while k < la:
        for i in range(0, la, 2*k):
            for j in range(i, i+k):
                x, y = a[j], a[j+k]
                a[j], a[j+k] = x + y, x - y
        k <<= 1
    return a
a = [1,3,5,2]
print(xorfft(a))