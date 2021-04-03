from collections import deque

n, t = map(int, input().split())
a = deque(map(int, input().split()))
b = deque(map(int, input().split()))

s = sum(a[i]*b[i] for i in range(n))

while s-t > 10:
	b.rotate()
	s = sum(a[i]*b[i] for i in range(n))






print(" ".join(str(i) for i in a))
print(" ".join(str(i) for i in b))
