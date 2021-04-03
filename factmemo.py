import sys
sys.setrecursionlimit(10**9)
def memoize_factorial(f): 
    memory = {} 
  
    # This inner function has access to memory 
    # and 'f' 
    def inner(num): 
        if num not in memory:          
            memory[num] = f(num) 
        return memory[num] 
  
    return inner 
      
#@memoize_factorial
def facto(num): 
    if (num == 0) or (num == 1): 
        return 1
    else: 
        return num * facto(num-1) 
facto = memoize_factorial(facto) # same as using @decorator i.e use this aur @ above
  
#print(facto(200))
