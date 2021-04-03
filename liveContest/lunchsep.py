def ans(a, n):
    while True:
        for i in range(n):
            if sum(a) == 0:
                print("YES")
                return
            
            elif sum(a) < 0:
                print("NO")
                return
            else:
                if a[i] > 0:
                    a[i] -= (i+1)

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans(a, n)
    
    
        