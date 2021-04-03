from collections import defaultdict
def subarrayXor(arr, n, m): 
    HashTable=defaultdict(bool)
    HashTable[0]=1
    count=0
    curSum=0
    for i in arr:
        curSum^=i
        if HashTable[curSum^m]:
            count+=HashTable[curSum^m]
        HashTable[curSum]+=1
    return(count)
def main(): 
    arr = [ 18, 4, 5, 2, 3, 9, 13 ] 
    n = len(arr) 
    m = 1
 
    print("Number of subarrays having given XOR is "
        , subarrayXor(arr, n, m)) 
 
if __name__ == '__main__': 
    main()


# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))
#     ans = 0
#     for i in range(n):
#     	if a[i]%2 == 0 :
#     		ans += 1
#     	x = a[i]
#     	for j in range(i+1, n):
#     		z = x^a[j]
#     		if (z)%2 == 0:
#     			# print(x^a[j])
#     			ans += 1
#     		x  = z
#     print(ans)
    			