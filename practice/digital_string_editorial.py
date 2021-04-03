min0 = min
PQRS = [0]*10**5
 
for _ in range(int(input())):
    N = int(input())
    d = [0]*4
    for i in range(N):
        PQRS[i] = tuple( map(int, input().split()))
    for i in range(4):
        d[i] = PQRS[0][i]
 
    for i in range(1, N):
        temp1 = PQRS[i][0] + min0(d[1] , d[2] , d[3])
        temp2 = PQRS[i][1] + min0(d[0] , d[2] , d[3])
        temp3 = PQRS[i][2] + min0(d[0] , d[1] , d[3])
        temp4 = PQRS[i][3] + min0(d[0] , d[1] , d[2])
        d[0] = temp1
        d[1] = temp2
        d[2] = temp3
        d[3] = temp4
    print(min0(d))