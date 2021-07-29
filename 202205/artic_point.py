graph = {}

def find_art_points(graph):
	visited = {n:False for n in graph}
	parent = {n: -1 for n in graph}
	disc = {n: float('inf') for n in graph}
	low = {n: float('inf') for n in graph}
	ap = {n: False for n in graph}
	t = 0
	
	def traverse(graph, v, disc, low, visited, p):
		nonlocal t
		nonlocal ap
		
		if visited[v] is False:
			visited[v] = True

			disc[v] = t
			low[v] = t
			t += 1
			
			
			children = 0
			
			for n in graph[v]:
				if visited[n] is False:

					children += 1
					traverse(graph, n, disc, low, visited, v)
					low[v] = min(low[v], low[n])
					
					if parent[v] == -1 and children >= 2:
						ap[v] = True
					
					if parent[v] != -1 and disc[v] >= low[n]:
						ap[v] = True
					
					
				elif n != parent[v]:
					low[v] = min(low[v], disc[n])
	
	
	for v in graph:
		if visited[v] is False:
			traverse(graph, v, disc, low, visited, -1)
	
	
	for n in ap:
		if ap[n] is True:
			print(n)
			
			
graph[0] = [1, 2, 3]
graph[1] = [0, 2]
graph[2] = [0, 1]
graph[3] = [0]

find_art_points(graph)


