# for i in range(int(input())):
#     n = int(input())
#     a  = []
#  
#     ans = 0
#     for i in range(n):
#         a.append(list(map(int, input().split())))

#    

#     for i in range(n):
#         for j in range(n):
#             for l in range(i, n):
#                 for m in range(j, n):
#                     if a[i][j] > a[l][m]:
#                         ans += 1



#     print(ans)
# def max1s(a):
#     best = 0
#     for i in range(len(a)):
INT_BITS = 32
def leftRotate(n, d): 
  
    # In n<<d, last d bits are 0. 
    # To put first 3 bits of n at  
    # last, do bitwise or of n<<d 
    # with n >>(INT_BITS - d)  
    return (n << d)|(n >> (INT_BITS - d))

def maxConsecutiveOnes(x) :  
  
    # Initialize result  
    count = 0;
  
    # Count the number of iterations to  
    # reach x = 0.  
    while (x != 0) : 
          
        # This operation reduces length  
        # of every sequence of 1s by one  
        x = (x & (x << 1));  
  
        count += 1;  
      
    return count

for i in range(int(input())):
    n, k = map(int, input().split())
    a = input()

    
    r

    
def leftRotate(s):
    temp = s[0]
    for i in range(1,len(s)):
        s[i-1] = s[i]
    s[-1] = temp
    return "".join(str(i) for i in s)

    




