import collections

# # general dict based graph for any hashabel type nodes
# class graph:
# 	def __init__(self, adj=None):
# 		if adj is None:
# 			adj = {}
# 		self.adj = adj




'''
Recursive BFS
Parameters:
	Graph G represented as adjacency list,
	Queue q,
	list seen of boolean values,
	integer key,

	Initially q has s node in it.

'''
def recursive_bfs(graph, q, seen, key):
	if not q:
		return False

	# pop front node from q and print it
	v = q.popleft()
	if v == key:
		return True

	# do for every neighbours of node v
	for u in graph[v]:
		if not seen[u]:
			seen[u] = True
			q.append(u)
	# recurse for other nodes
	return recursive_bfs(graph, q, seen, key)

# g = [[1,2], [0,2], [3,1], [0,1]]
g = [[], [0, 2], [1]]
seen = [False]*len(g)
key = 2
q = collections.deque()
source = 1
q.append(source)
seen[0] = True
print(recursive_bfs(g, q, seen, key))


'''
Iterative BFS
Parameters:
	Graph graph,
	source node s,
	list seen,
	intger key,

'''

def iterative_bfs(graph, s, seen, key):
	# create a queue needed for bfs
	q = collections.deque()

	# mark source node as seen
	seen[s] = True

	# add source node into q
	q.append(s)
	while q:
		v = q.popleft()
		if v == key:
			return True
		# for every neighboring node of v
		for u in graph[v]:
			if not seen[u]:
				seen[u] = True
				q.append(u)
	return False

# g = [[1,2], [0,2], [3,1], [0,1]]
g = [[], [0, 2], [1]]

seen = [False]*len(g)
key = 2
source = 0

print(iterative_bfs(g, source, seen, key))