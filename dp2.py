from array import array
def memoize_num(func):
		memory = {}

		def inner(num):
			if num not in memory:
				memory[num] = func(num)
			return memory[num]

		return inner


@memoize_num
def solve(num):
	if len(str(num)) == 1:
		return 1
	if len(str(num)) == 2:
		return 2 if (num%100 < 27 ) and (num%100 > 0) and (num != 10) and (num != 20) else 1
	elif num%100 == 10 or (num%100 == 20):
		return solve(num//100)
	elif len(str(num%100)) == 1:
		return solve(num//100)
	elif (num%100 < 27) and (num%100 > 0):
		return solve(num//10) + solve(num//100)
	else:
		return solve(num//10)
			
while True:
	inp = int(input())
	if inp == 0:
		break

	s = solve(inp)
	print(s)

	


		

	
		

