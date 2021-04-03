from random import randint, shuffle, choice
# from collections import Counter
# print(10)
# for _ in range(10):
# 	n = 49
# 	print(n)
# 	a = [randint(0, 10**5) for i in range((n//2))]
# 	a *= 2
# 	a.append(randint(10**5 + 1, 10**5 + 200))
# 	shuffle(a)
# 	print(*a)
	# print(Counter(a))



# t1 = 1000
# print(t1)
# for _ in range(t1):
# 	a = [randint(1, 1000) for i in range(4)]
# 	print(*a)

# t2 = 10
# print(t2)
# for _ in range(t2):
# 	a = [randint(1, 10**8) for i in range(4)]
# 	print(*a)

# t1 = 100
# print(t1)
# for _ in range(t1):
# 	print(randint(1, 10**5))

# t2 = 50
# print(t2)
# for _ in range(t2):
# 	print(randint(1, 10**12))


# t = 10**5
# print(t)
# for _ in range(t):
# 	a = randint(0, (10**8)-1)
# 	b = randint(a+1, (10**8))
# 	k = randint(0, 10**8)
# 	assert a < b
# 	print(a, b, k)


# t = 10**3
# print(t)
# for _ in range(t):
# 	a = randint(0, (10**4)-1)
# 	b = randint(a+1, 10**4)
# 	k = randint(0, 10**4)
# 	assert a < b
# 	print(a, b, k)
from string import ascii_letters
lower = ascii_letters+" "
t = 25
print(t)
for _ in range(t):
	n = randint(1, 30)
	s = [choice(lower) for i in range(n)]
	print("".join(s))
# t = 100
# print(t)
# for _ in range(t):
# 	s = [choice(lower) for i in range(100)]
# 	m = [choice(lower) for i in range(50)]
# 	a = m*2
# 	assert len(s) == 100
# 	assert len(a) == 100
# 	print(choice(["".join(s), "".join(a)]))

# t = 10**4
# print(t)

# for _ in range(t):
# 	s = [choice(lower) for i in range(100)]
# 	m = [choice(lower) for i in range(500)]
# 	a = m*2
# 	assert len(a) == 10**3
# 	assert len(s) == 100

# 	# l = print("".join(s))
# 	# k = print("".join(a))
# 	l = "".join(s)
# 	k = "".join(a)
# 	print(choice([l, k]))