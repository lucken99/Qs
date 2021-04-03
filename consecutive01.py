# # Python3 program to implement
# # the above approach
 
# # Function to count binary 
# # Strings that satisfy the 
# # given condition
# def cntBinStr(N, P, Q):
   
#     # zero[i][j] stores count
#     # of binary Strings of length i
#     # having j consecutive 0s
#     zero = [[0 for i in range(P)] 
#                for j in range(N + 1)];
 
#     # one[i][j] stores count
#     # of binary Strings of length i
#     # having j consecutive 1s
#     one = [[0 for i in range(Q)] 
#               for j in range(N + 1)];
 
#     # Base case
#     zero[1][1] = one[1][1] = 1;
 
#     # Fill all the values of 
#     # zero[i][j] and one[i][j] 
#     # in bottom up manner
#     for i in range(2, N + 1):
#         for j in range(2, P):
#             zero[i][j] = zero[i - 1][j - 1];
 
#         for j in range(1, Q):
#             zero[i][1] = (zero[i][1] +
#                           one[i - 1][j]);
 
#         for j in range(2, Q):
#             one[i][j] = one[i - 1][j - 1];
 
#         for j in range(1, P):
#             one[i][1] = one[i][1] + zero[i - 1][j];
 
#     # Stores count of binary 
#     # Strings that satisfy 
#     # the given condition
#     res = 0;
 
#     # Count binary Strings of
#     # length N having less than
#     # P consecutive 0s
#     for i in range(1, P):
#         res = res + zero[N][i];
 
#     # Count binary Strings of
#     # length N having less than
#     # Q consecutive 1s
#     for i in range(1, Q):
#         res = res + one[N][i];
 
#     return res;

# if __name__ == '__main__':
   
#     N = 2;
#     P = 2;
#     Q = 3;
#     print(cntBinStr(N, 2, N+1));

def count0(n):
    a = [0 for i in range(n)]
    b = [0 for i in range(n)]
    a[0] = b[0] = 1
    for i in range(1, n):
        a[i] = a[i-1] + b[i-1]
        b[i] = a[i-1]
    return a[n-1] + b[n-1]
print(count0(2))