
# -------------------------------- input
G = Graph({
	'a': { 'b': 4, 'h': 8 },
	'b': { 'c': 8, 'h':11 },
	'c': { 'd': 7, 'f': 4, 'i': 2 },
	'd': { 'e': 9, 'f': 14 },
	'e': { 'f': 10 },
	'f': { 'g': 2 },
	'g': { 'h': 1, 'i': 6 },
	'h': { 'i': 7 },
})
T = Graph([
	('g', 'h', 1),
	('f', 'g', 2),
	('c', 'i', 2),
	('c', 'f', 4),
	('s', 'b', 4),
	('c', 'd', 7),
	('b', 'c', 8),
	('d', 'e', 9),
])
new_edge = ('b', 'e', 1)

# -------------------------------- logic
def add_edge(graph, e):
	graph.add_edge(e)
	print('Aresta adicionada', e)

def dfs(graph):
	visited = set()
	finished = set()

	def dfs_visit(vertex, parent):
		visited.add(vertex)
		print('Vértice visitado:', vertex)
		for neighbor in graph.neighbors(vertex):
			if neighbor == parent:
				continue
			elif neighbor not in visited:
				dfs_visit(neighbor, vertex)
			elif neighbor not in finished: # visited but not finished
				print('Ciclo encontrado')
				return
		finished.add(vertex)
		print('Vértice finalizado:', vertex)

	for vertex in graph.vertices():
			if vertex not in visited:
				dfs_visit(vertex, None)

	return visited, finished

def recalc_mst(mst, new_edge):
	add_edge(mst, new_edge)

	_, finished_vertices = dfs(mst)

	not_finished_edges = []
	for edge in mst.edges(labels=True):
		u, v, w = edge
		if u not in finished_vertices or v not in finished_vertices:
			not_finished_edges.append((u, v, w))
			print('Aresta não finalizada', edge)

	if not_finished_edges:
				edge_to_remove = max(not_finished_edges, key=lambda x: x[2])
				mst.delete_edge(edge_to_remove[:2])
				print('Removida aresta de maior peso:', edge_to_remove)

	return mst

# -------------------------------- execution
#add_edge(G, new_edge)
print('Old MST:', T.edges())
new_mst = recalc_mst(T, new_edge)
print('New MST:', new_mst.edges())
