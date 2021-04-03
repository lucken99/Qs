# https://www.hackerearth.com/challenges/competitive/december-circuits-20/algorithm/move-minimization-8a9d3991/

def bubbleSort(arr): 
	n = len(arr)
	ans = 0

	# Traverse through all array elements 
	for i in range(n): 
	    swapped = False

	    # Last i elements are already 
	    #  in place 
	    for j in range(0, n-i-1): 

	        # traverse the array from 0 to 
	        # n-i-1. Swap if the element  
	        # found is greater than the 
	        # next element 
	        if arr[j] > arr[j+1] : 
	            arr[j], arr[j+1] = arr[j+1], arr[j] 
	            swapped = True
	            ans += 1

	    # IF no two elements were swapped 
	    # by inner loop, then break 
	    if swapped == False: 
	        return ans

n = int(input())
p = list(map(int, input().split()))

arr = [(p[i]-(i+1),i) for i in range(n)]

arr.sort()
# print(arr)
ma = arr[-1]
mi = arr[0]

p[ma[1]], p[mi[1]] = p[mi[1]], p[ma[1]]
print(bubbleSort(p))

# s.sort()
# print(s[-2])

# print(s)