import random
from random import randint, choice, sample, shuffle
# n = int(input())
# for _ in range(t):

# 	l = randint(1,10**7)
# 	print(l, randint(l, 10**7), randint(1,9))
# 	

# print(1)
# print(100000)
# for i in range(1, 100001):
# 	print(i, end=" ")
# print()
# n = int(input())
# # print(t := int(input()))
# print(2000)
# for _ in range(2000):
# 	k = randint(0, 10**5)
# 	print(n, k)
# 	for i in range(n):
# 		print(choice("IM_:X"), end= "")
# 	print()


# print(randint(1,100), randint(1,100), randint(1,100), randint(1,100), randint(1,1000))

# print(10)
# for _ in range(10):
# 	n = randint(2, 50)
# 	x = randint(1, 1000)
# 	print(n, x)
# 	for i in range(n):
# 		print(randint(1, 50), end=" ")
# 	print()

# for i in range(20):
# 	print("".join(choice(['0', '1']) for i in range(randint(4, 20))))
# print(t:=int(input()))



# t = 10
# print(t)
# for i in range(t):
# 	n, k = randint(1, 4000), randint(1, 4000)
# 	print(n, k)
# 	h = [randint(1 ,50) for i in range(n)]
# 	print(*h)

# print(5)
# for _ in range(5):
# 	n = 10**5
# 	q = randint(1, 10**5)
# 	print(n, q)
# 	a = [randint(1, 10**9) for i in range(n)]
# 	print(*a)
	
# 	for i in range(q):
# 		print(choice(a))

# print(1000000)
# for _ in range(1000000):
# 	print(randint(1, 1000000), randint(2, 1000000))

# Binary search
# subtask 1
# t = 10
# print(t)
# for _ in range(t):
# 	n = randint(1, 5000)
# 	type = randint(-10000, 10000)
# 	print(n, type)
# 	# a = [randint(-10000, 10000) for i in range(n)]
# 	a = sample(range(-10000, 10000), n)
# 	a[randint(0, n-1)] = type
# 	assert len(set(a)) == n
# 	print(*a)

# t = 2
# print(t)
# for _ in range(t):
# 	n = randint(1, 10000000)
# 	type = randint(-100000, 100000)
# 	print(n, type)
# 	a = sorted(sample(range(-100000000, 100000000), n))
# 	assert len(set(a)) == n
# 	print(*a)


import string
# print(100)
# for _ in range(100):
# 	n = randint(1, 25)
# 	s1 = "".join(choice(string.ascii_letters) for i in range(n))
# 	n = randint(1, 25)
# 	s2 = "".join(choice(string.ascii_letters) for i in range(n))
# 	print(choice("ABCDEFGH"), s1, s2)


print(10)
for t in range(10):
	n = randint(1, 1000)

	s1 = [choice(string.ascii_lowercase) for i in range(n)]
	# n = randint(1, 1000)
	s2 = [choice(string.ascii_lowercase) for i in range(n)]
	s2 = choice([s1, s2])
	shuffle(s2)
	s3 = [choice(string.ascii_lowercase) for i in range(n)]
	s3 = choice([s1, s2, s3])
	shuffle(s3)
	shuffle(s1)
	shuffle(s2)
	s1 = "".join(s1)
	s2 = "".join(s2)
	s3 = "".join(s3)

	print(s1, s2, s3)



print(10)
for t in range(10):
	n = randint(1, 1000000)

	s1 = [choice(string.ascii_lowercase) for i in range(n)]
	# n = randint(1, 1000)
	s2 = [choice(string.ascii_lowercase) for i in range(n)]
	s2 = choice([s1, s2])
	shuffle(s2)
	s3 = [choice(string.ascii_lowercase) for i in range(n)]
	s3 = choice([s1, s2, s3])
	shuffle(s3)
	shuffle(s1)
	shuffle(s2)
	s1 = "".join(s1)
	s2 = "".join(s2)
	s3 = "".join(s3)

	print(s1, s2, s3)