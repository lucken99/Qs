for _ in range(int(input())):
	n = int(input())
	b = input()
	one = b.count('1')
	if ((one + 120 - n)*100)/120 >= 75:
		print("YES")
	else:
		print("NO")

# wrong
# for _ in range(int(input())):
# 	x, y, k, n = map(int, input().split())
# 	if abs(x-y) == k*2:
# 		print("Yes")
# 	else:
# 		print("No")

for i  in range(int(input())):
    x,y,k,n=list(map(int,input().split()))
    if abs(x-y)%2==0:
        a=abs(x-y)/2
        if a%k==0:
            print("Yes")
        else:
            print("No")
    else:
      print("No")

# wrong
# for _ in range(int(input())):
# 	s = input()
# 	one = s.count('1')
# 	zero = s.count('0')

# 	if len(s)&1:
# 		print(-1)
# 	else:
# 		print(abs(one-zero)//2)

