# import math 
# def is_perfect(num, power):
#     float_candidate = num ** (1/power)
#     int_candidate = int(math.floor(float_candidate))
#     while True:
#         powered = int_candidate ** power
#         if powered == num: return True
#         elif powered > num: return False
#         int_candidate += 1

# n, k, q = map(int, input().split())
# a = list(map(int, input().split()))
# queries = []
# for i in range(q):
#     queries.append(list(map(int, input().split())))
# for i in queries:
#     if i[0] == 1:
#         z=1
#         for j in range(i[1]-1, i[2]):
#             z *= a[j]
#         if is_perfect(z, k):
#             print("Yes")
#         else:
#             print("No")
#     elif i[0] == 2:
#         for j in range(i[1]-1, i[2]):
#             a[j] *= (i[3]**i[4])
#     else:
#         for j in range(i[1]-1, i[2]):
#             a[j] = i[3]



# n = int(input())
# a = list(map(int, input().split()))
# q = int(input())
# qi = []

# for i in range(q):
    
#     qi.append(list(map(int, input().split())))

# for i in qi:
#     ans = float('INF')
#     m = len(bin(max(a[i[0]-1:i[1]])))-2
#     for k in range(m):
#         z = 0
#         for j in range(i[0]-1, i[1]):
#             if not a[j]&(1<<k):
#                 z += 2**k
#         ans = min(ans,z)
#     print(ans)

import math

# def is_perfect(num, power):
#     candidate = num ** (1/power)
#     lo_candidate = int(math.floor(candidate))
#     hi_candidate = int(math.ceil(candidate))
#     return num == lo_candidate**power or num == hi_candidate**power

# def kthRoot(num, k):
#     if k == 1:
#         return num;
#     start = 0
#     end = num
#     mid=0
#     sol=0

#     while(start <= end):
#         mid = (start + end)/2;
#         ans = pow(mid, k);
#         if(ans == num):
#             sol = mid;
#             break;
#         elif(ans < num):
#             start = mid+1;
#             sol = mid;
#         else:
#             end = mid-1;
#     return sol;

# n, k, q = map(int, input().split())
# a = list(map(int, input().split()))
# queries = []
# for i in range(q):
#     queries.append(list(map(int, input().split())))
# for i in queries:
#     if i[0] == 1:
#         z=1
#         for j in range(i[1]-1, i[2]):
#             z *= a[j]

#         result = kthRoot(z, k);
#         if(pow(result, k) == z):
#             print("Yes")
#         else:
#             print("No\n")

#     elif i[0] == 2:
#         for j in range(i[1]-1, i[2]):
#             a[j] *= (i[3]**i[4])
#     else:
#         for j in range(i[1]-1, i[2]):
#             a[j] = i[3]

# private static long AddToEnsureOne(long value, int position) {
#     if ((value & (1L << position)) != 0)
#       return 0;

#     long shift = 1L << (position);

#     return shift - (value & (shift - 1)); 
#   }

#   private static long MinToAdd(IEnumerable<int> items) {
#     long best = 0;

#     for (int i = 0; i < 32; ++i) {
#       long sum = 0;

#       foreach (int item in items)
#         sum += AddToEnsureOne(unchecked((uint)item), i); // uint - get rid of sign

#       if (i == 0 || sum < best)
#         best = sum;
#     }

#     return best;
#   }


def one(v, pos):
    if v&(1<<pos) != 0:
        return 0
    shift = 1<<pos
    return shift - (v&(shift-1))

def ans(a):
    best = 0
    for i in range(32):
        sum = 0
        for j in a:
            sum += one(j, i)
        if (i==0) or (sum < best):
            best = sum
    return best


ind2 = []
    try:
        i  = b.index('.'*m)
        ind2.append(i)
    except:
        maxi2 = max(len(b[0].replace(".","")), len(b[-1].replace(".","")))
    try:
        while i < n:
            i = b.index('.'*m, i+1)
            ind2.append(i)
    except:
        pass
    maxi2 = max(len(b[0].replace(".","")), len(b[-1].replace(".","")))
    for i in range(len(ind2)):
        if ind2[i] == n-1:
            maxi2 = max(len(b[ind2[i]-1].replace(".", "")), maxi2)
        elif ind2[i] == 0:
            maxi2 = max(len(b[1].replace(".", "")), maxi2)
        else:
            maxi2 = max(len(b[ind2[i]-1].replace(".", "")), len(b[ind[i]+1].replace(".", "")), maxi2)