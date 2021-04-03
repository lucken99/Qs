
TIME = [0]*10**3
d = [0]*4
 

N = int(input())
for i in range(N):
    TIME[i] = tuple( map(int, input().split()))

d[0] = 1
server = 1
TIME = sorted(TIME[:N])
for i in range(1, N):
    for j in range(i):
        count = 0
        if (TIME[j][2] <= TIME[i][0]) and ((TIME[i][1] - TIME[j][3]) >= 5):
            pass
        else:
            count += 1
    d[i] =  count - d[i-1]
print(sum(d))