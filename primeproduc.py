# def primeproduct(n):
#     if n>=2:
#         def factors(n):
#             factlist=[]
#             for i in range(2,n+1):
#                 if n%i==0:
#                     factlist.append(i)
#             return factlist
#         fac=factors(n)
#         if len(fac)==2:
#             if(len(factors(fac[1]))==1):
#                 return True
#             else:
#                 return False
#         elif len(fac)==3:
#             if(len(factors(fac[1]))==1):
#                 return True
#             else:
#                 return False
#         else:
#             return False
#     else:
#         return False
def primeproduct(n):
    if n>=2:
        def factors(n):
            factlist=[]
            for i in range(2,n+1):
                if n%i==0:
                    factlist.append(i)
            return factlist
        fac=factors(n)
        if len(fac)==2:
            if(len(factors(fac[0]))==1):
                return True
            else:
                return False
        elif len(fac)==3:
            if(len(factors(fac[1]))==1):
                return True
            else:
                return False
        else:
            return False
    else:
        return False 
for i in range(int(input())):
    n = int(input())
    print(primeproduct(n))