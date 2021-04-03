def lsb(i):
	# ans = 0
	# b = list(reversed(bin(i)[2:]))
	# for j in range(len(b)):
	# 	if b[j] == '1':
	# 		ans = j
	# 		break
	# return 2**ans

	return i & -i

#print(lsb(16))

# fenwick tree construction
def construct(values): # make sure values is 1-based
	n = len(values)
	tree = a[:]
	for i in range(1, n+1):
		j = i + lsb(i)
		if j < n:
			tree[j] += tree[i]
	return tree

# prefix sum (dynamic)
def prefix_sum(i):
	sum = 0
	while i != 0:
		sum += tree[i]
		i = i - lsb(i)  # or we can write (i & ~lsb(i))
	return sum

# range sum query
def range_query(i, j):
	return prefix_sum(j) - prefix_sum(i-1)

# point update algorithm
def add(i, x):
	while i < n:
		tree[i] += x
		i = i + lsb(i)

a = [0, 1, 5, 7, 8, -4, 5, -1] # index 0 is not included we include
								# this to make 1 based index

a = [0, 3, 4, -2, 7, 3, 11, 5, -8, -9, 2, 4, -8]
tree = [0 for i in range(len(a)+1)]
n = len(tree)

tree = construct(a)

print(tree)
add(1, 1)
print(tree)
ans = range_query(1,5)
print(ans)





