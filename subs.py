def lengthOfLIS(nums):

        def binarySearch(sub, val):
            lo, hi = 0, len(sub)-1
            while(lo <= hi):
                mid = lo + (hi - lo)//2
                if sub[mid] <= val:
                    lo = mid + 1
                elif val < sub[mid]:
                    hi = mid - 1
                else:
                    return mid
            return lo
        
        sub = []
        for val in nums:
            pos = binarySearch(sub, val)
            if pos == len(sub):
                sub.append(val)
            else:
                sub[pos] = val
        return len(sub)


for _ in range(int(input())):
    n = int(input())
    str = input()
    a = list(map(int, str))
    # print(a)
    if "".join(sorted(str)) == str:
        print(0)
    elif "".join(sorted(str)) == str[::-1]:
        print(min(str.count('0'), str.count('1')))
    
    else:
        print(n - lengthOfLIS(a))