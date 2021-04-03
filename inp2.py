import io, os
from sys import stdin, stdout

reader = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
print = stdout.write

a = []
for i in range(1000000):
	a.append(int(reader().decode()))

for i in range(len(a)):
	print(str(a[i])+'\n')