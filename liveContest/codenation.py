def answer():
    ans  = 0
    def minCost(arr, n):
            cost = 9999999
            xor = 0
            for i in range(0, n):
                xor ^= arr[i]
                
            # if xor == 0:
            #     return False
            # return True
            
            for i in range(n):
                if (cost > abs((xor ^ arr[i]) - arr[i])):
                    cost = abs((xor ^ arr[i]) - arr[i])
                    elem = i
            return elem, abs(cost)
        ans = 0
        z = float('INF')
        ind = 0
        for i in range(0, len(A)-k+1):
            if i%k == 0:
                ind += k
            e, c = minCost(A[i:i+k], k)
            if c != 0:
                if i != 0:
                    if (e+ind) != z:
                        ans += 1
                        z = e + ind
                else:
                    if e != z:
                        ans+1 
                        z = e
                        
        return ans
    return ans