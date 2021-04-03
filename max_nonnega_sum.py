def max_noneg_contiguous(a):
	n = len(a)
	maxi = 0
	sum = 0
	for i in range(n):

		if a[i] < 0:
			sum = 0
		else:
			sum += a[i]
			maxi = max(maxi, sum)
	return maxi
#wrong for edge cases
# def max_noneg_contiguous_subarray(a):
# 	n = len(a)
# 	j = 0
# 	sums = 0
# 	maxi = [0]
# 	ans = []
# 	for i in range(n):
# 		if a[i] < 0:
# 			ans = []
# 		else:
# 			ans.append(a[i])
# 		if sum(ans) > sum(maxi):
# 			maxi = ans[:]
# 	return maxi

#right
def maxset(A):
    maxsumlist = []
    cursumlist = []
    maxsum = 0
    currsum = 0
    for i in A:
        if (i >= 0):
            currsum = currsum + i
            cursumlist.append(i)
            if(currsum > maxsum):
                maxsum = currsum
                maxsumlist = cursumlist
            elif(currsum == maxsum):
                if(len(cursumlist) > len(maxsumlist)):
                    maxsumlist = cursumlist
            #elif(len(cursumlist))
                    
        elif(i<0):
            currsum = 0
            cursumlist = []
                
    return maxsumlist



print(max_noneg_contiguous_subarray([1,4,-3,9,5,-6, 4, 5, 8, -1, -2,  -4, -5, 58]))
print(max_noneg_contiguous([12,0,10,3,11,-1,25,12]))
print(max_noneg_contiguous_subarray([0,0,-1,0]))
print(max_noneg_contiguous_subarray([-1, -1, -1]))