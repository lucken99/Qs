
prefix = []
prefix.append(0)
prefix.append(0)
def SieveOfEratosthenes(n):
 
    # Create a boolean array 
    # "prime[0..n]" and initialize
    #  all entries it as true.
    # A value in prime[i] will
    # finally be false if i is 
    # Not a prime, else true.
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
 
        # If prime[p] is not 
        # changed, then it is a prime
        if (prime[p] == True):
 
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    
    ans = 0
    for p in range(2, n+1):
        if prime[p]:
            ans += 1
        prefix.append(ans)

SieveOfEratosthenes(1000001)
print(prefix)


# for _ in range(int(input())):
#     x, y = map(int, input().split())
#     c = prefix[x]
#     if c <= y:
#         print("Chef")
#     else:
#         print("Divyam")


