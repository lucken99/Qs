def solve(A, B):
    ans = []
    for i in range(len(B)):
        l, r = B[i][0], B[i][1]
        rA = A[::-1]
        lengthA = len(A)
        
        try:
            lind = A.index('1',l-1,r-1)
            rtemp = rA.index('1',lengthA-r, lengthA-l)
            rind =  lengthA-rtemp-1
            
            if lind != rind:
                ans.append(A.count('0', lind, rind))
            elif lind == rind:
                ans.append(0)
                
        except:
            ans.append(0)
    return ans


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        number = 0
        if B<=C:
            return 0
        else:
            for i in range(B,2,-1):
                if (B%i==0) and (B//i >C) and ((B//i + i*(i-1)) == B):
                    number = i
                    break