#Wrong
def min_sec(m1, m2, ind):
	m1 = m1[:]
	m2 = m2[:]
	if m2.index(min(m2)) == ind:
		m2[ind] = float("inf")
		ind = m2.index(min(m2))
		return min(m2), ind
	ind = m2.index(min(m2))
	return min(m2), ind

def Solve(N,PQRS):
	#write your code here
	#return your answer
	a = [0 for i in range(N)]

	a[0] = min(PQRS[0])
	ind = PQRS[0].index(min(PQRS[0]))
	for i in range(1, N):
		mini, ind = min_sec(PQRS[i-1], PQRS[i], ind)
		a[i] = a[i-1] + mini
	return a[N-1]


T = int(input())
for _ in range(T):
	
	N = int(input())
	
	PQRS = []
	for i in range(N):
		PQRS.append(list(map(int,input().split())))
	
	out_ = Solve(N,PQRS)
	print (out_)
