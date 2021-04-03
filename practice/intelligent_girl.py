def solve(s):
    a = [0 for i in range(len(s))]
    a[-1] = 1 if a[-1]%2==0 else 0
    for i in reversed(range(len(s)-1)):
        a[i] = a[i+1] + 1 if s[i]%2==0 else a[i+1]
    return a

        


     
s = list(map(int, input()))
ans = solve(s)
print(" ".join(str(i) for i in ans))