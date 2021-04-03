import sys

input = sys.stdin.readline



# for _ in range(int(input())):
# 	# n = int(input())
# 	i = 1
# 	flag = False
# 	while True and not flag:
# 		print(i**2)
# 		x = int(input())
# 		if x==1:
# 			break
# 		elif x == -1:
# 			flag = True
# 			print("Wrong Verdict")
# 		else:
# 			i += 1

for _ in range(int(input())):
    n, m, k = map(int, input().strip().split())
    x = 0
    a = [[0]*10**6 for i in range(10**6)]
    for i in range(n):
    	for j in range(m):
    		x ^= k+i+j+2
    print(x)