def is_bipartite_graph_using_dfs(adj, v, seen, color):
	for u in adj[v]:
		# if vertex u is not explored before
		if seen[u] == False:
			seen[u] = True

			# Mark present vertex color opposite to its parent
			color[u] = not color[v]

			# if the subtree rooted at vertex v is not bipartite
			if not is_bipartite_graph_using_dfs(adj, u, seen, color):
				return False


		# if two adjacent are colored with same color then the graph is not bipartite
		elif color[u] == color[v]:
			return False

	return True


