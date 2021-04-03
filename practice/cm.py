import sys
sys.setrecursionlimit = 10**6
def memoize_factorial(f): 
    memory = {} 
  
    # This inner function has access to memory 
    # and 'f' 
    def inner(num): 
        if num not in memory:          
            memory[num] = f(num) 
        return memory[num] 
  
    return inner 
      
@memoize_factorial
def facto(num): 
    if num == 1: 
        return 1
    else: 
        return num * facto(num-1) 
# facto = memoize_factorial(facto)



t = int(input())

while t:
	t -= 1
	n = int(input())
	s = input()

	vowel = 0
	for i in s:
		if i in "AEIOU":
			vowel += 1
	if vowel:
		ways = facto(vowel) * facto(n-vowel+1)
	else:
		ways = facto(n - vowel)

	print(ways)




