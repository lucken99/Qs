for _ in range(int(input())):
	n, m = map(int, input().split())
	a = []
	for i in range(m):
		a.append(list(map(int, input().split())))
	a.sort()
	ans = 0
	maxi = 0
	t = 0
	j = 0
	while j < m-1:
		for i in range(m-1):
			if a[j][1] != a[j+1][0]:
				t += 1
				break
				
			t += 1
		
		j += t
		
		ans += 1
	print(ans)

import sys 
sys.setrecursionlimit(10**5)
from collections import defaultdict

g = defaultdict(list)

def dfs(u,visited):
    visited[u] = True 
    for v in g[u]:
        if not visited[v]:
            dfs(v,visited)
            

for _ in range(int(input())):
    (n,m) = map(int,input().split())
    g.clear()
    
    for _ in range(m):
        (u,v) = map(int,input().split())
        g[u].append(v)
        g[v].append(u)
    
    visited = [False]*n 
    ans = 0 
    for i in range(n):
        if not visited[i]:
            ans += 1
            dfs(i,visited)
    print(ans)



