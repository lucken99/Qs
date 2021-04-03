from functools import wraps

def memo(func):
	cache = {}
	@wraps(func)
	def wrap(*args):
		if args not in cache:
			cache[args] = func(*args)
		return cache[args]
	return wrap


@memo
def solve(a, b, m, n):
	if m == 0 or n == 0:
		return 0
	elif a[m-1] == b[n-1]:
		return 1+solve(a, b, m-1, n-1)
	return max(solve(a, b, m, n-1), solve(a, b, m-1, n))

#a = ['l', 'k','a', 'k', 'a', 'k']
#b = ['l', 'k', 'k', 'a', 'k']
a  = 'aaAGGTABaassdabsssssssssssssssbdddddddnsbdsndndnnbjhcbsaccsacksdckjclkjhgggggggggggggggggggggggggggggggggggnnnmmmaaaaaaaagaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaannnnnnnnnnnnnnnnnnnnnnnnnnnnnnnsssssssssssssssssssssssssssssaaaaaaaaaaaaaaaaaaaaaaaaaaannnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnln'
b = 'aaGXlkjaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaassssssssssssssssssssssssssssssaaaaaaaaannnnnnnggnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnsssssssssssssssskdjdhffgggggggggggggggggggggadTXAYB'
print(solve(a, b, len(a), len(b)))
#print(solve(a, b, len(a), len(b)))