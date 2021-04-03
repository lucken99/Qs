# for _ in range(int(input())):
# 	n, d = map(int, input().split())
# 	a = list(map(int, input().split()))
# 	a.sort()
# 	if a[-1] <= d or a[0]+a[1]<=d:
# 		print("YES")
# 	else:
# 		print("NO")

def gcd(a,b):
    if a == 0:
        return b
    return gcd(b % a, a)
 
# Function to return LCM of two numbers
def lcm(a,b):
    return (a / gcd(a,b))* b


for _ in range(int(input())):
	s = input()
	t = input()

	ls = len(s)
	lt = len(t)

	if set(s) == set(t):
		print(str(set(s))*lcm(ls, lt))
	else:
		if ls < lt:
			for i in range(1, 1000):
				if ls*i == lt:
