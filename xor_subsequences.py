from sys import stderr
from itertools import accumulate
from operator import xor

MAXNUM = 1 << 16

def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    c = [0] * MAXNUM
    for elt in accumulate(a, xor):
        c[elt] += 1
    c[0] += 1
    conv = xorfft(i * i for i in xorfft(c))
    conv[0] = 2 * MAXNUM * sum(i * (i-1) // 2 for i in c)
    print(conv)
    ans = max((v , -i) for i, v in enumerate(conv))
    print(-ans[1], ans[0] // (2 * MAXNUM))

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

main()
