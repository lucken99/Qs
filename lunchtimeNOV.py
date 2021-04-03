# def solve(f, n):
# 		ans = f[0]
# 		for i in range(1, n):
# 			ans -= 1
# 			if ans < 0:
# 				# return i-1
# 				return False
# 			else:
# 				ans += f[i]
# 				if ans <= 0:
# 					# return i
# 					return False
# 		# return i + (ans)
# 		return True



# for _ in range(int(input())):
# 	n = int(input())
# 	f = list(map(int, input().split()))


	# print(solve(f, n))


# for _ in range(int(input())):
# 	n = int(input())
# 	f = list(map(int, input().split()))
# 	c = list(map(int, input().split()))
# 	d = [(f[i]*c[i], i) for i in range(n)]
# 	d.sort(key=lambda x:x[0])

	
# 	for i in d:
# 		if solve(f[])


# XOR
# for _ in range(int(input())):
# 	x, y, n = map(int, input().split())
# 	c= 0
# 	for i in range(n+1):
# 		if (x^i) < (y^i):
# 			# print(x^i, y^i)
# 			# print((x,i), (y,i))
# 			c += 1
# 	print(c)

# def din(st):
#     return bin(st)[2:].zfill(10)


f = input


def func(x, y, n):
    # count = 0
    # for z in range(0, n+1):
    #     print(din(x), "xor", din(z), end=" ")
    #     if x ^ z < y ^ z:
    #         count += 1
    #         print("<", end=" ")
    #     else:
    #         print(">=", end="")
    #     print(din(y), "xor", din(z), "z =", z)
    z0 = x ^ 0 < y ^ 0
    unmatch = 1
    # print(z0)
    # print((x ^ unmatch < y ^ unmatch))
    while z0 == (x ^ unmatch < y ^ unmatch) and unmatch < n+1:
        # print(unmatch < n+1)
        unmatch *= 2
        # print("unmatch =", unmatch)
    # print("x y =", x, y)
    # print("unmatch =", unmatch)
    # print("n =", n)
    ans = ((n+1) // (unmatch*2)) * unmatch
    ans += min(unmatch, (n+1)-(ans*2))
    # print("ans =", ans)
    return (ans if z0 else ((n+1)-ans))


for _ in range(int(f())):
    x, y, n = map(int, f().split())
    # x, y = (randint(1, 20), randint(1, 20))
    print(func(x, y, n))




# from math import gcd
# n = int(input())
# c = 0
# for i in range(1,n+1):
# 	for j in range(1,n+1):
# 		a = i*(j+1)
# 		b = (i+1)*j
# 		g = gcd(a,b)
# 		a //= g
# 		b //= g
# 		if a - b == 1:
# 			c += 1
# print(c)
