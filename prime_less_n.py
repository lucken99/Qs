import math
def approx_num_of_prime(n):
	return round(n/math.log(n))

print(approx_num_of_prime(1000000))

# for _ in range(int(input())):
#     x, y = map(int, input().split())
#     c = approx_num_of_prime(x)
#     if c <= y:
#         print("Chef")
#     else:
#         print("Divyam")