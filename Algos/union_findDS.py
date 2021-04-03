size = 0
sz = []
ids = []

numComponents = 0


for i in range(size):
	ids.append(i)
	sz.append(1) 

def find(p):
	root = p
	while root != ids[root]:
		root = ids[root]

	# compression
	while p != root:
		nexti = ids[p]
		ids[p] = root
		p = nexti

	return root


def coonected(p, q):
	return find(p) == find(q)

def componentSize(p):
	return sz[find(p)]

def size():
	return size

def components():
	return numComponents

def unify(p, q):
	root1 = find(p)
	root2 = find(q)

	if root1 == root2:	return

	if sz[root1] < sz[root2]:
		sz[root2] += sz[root1]
		ids[root1] = root2
	else:
		sz[root1] ++ sz[root2]
		ids[root2] = root1

	numComponents -= 1

