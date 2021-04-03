#n =  250
n = 1000000000000000000000000000000000000000000000000000000000000000000000000000000
#dp = [-1 for i in range(n)]

def memoize_coin(func):
	memory = {}

	# This inner function has access to memory and 'func'
	def inner(num):
		if num not in memory:
			memory[num] = func(num)
		return memory[num]
	return inner

@memoize_coin
def solve(n):
	if n <= 11:
		return n

	return solve(n//2) + solve(n//3) + solve(n//4)
p = solve(n)
print(p)