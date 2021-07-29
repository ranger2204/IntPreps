def alien_dictionary(words):
		
	graph = {}
	
	for w in words:
		for c in w:
			graph[c] = []
		
	for i in range(1, len(words)):
		w_prev = words[i-1]
		w_cur = words[i]
		
		max_len = min(len(w_prev), len(w_cur))
		for i in range(max_len):
			if w_prev[i] == w_cur[i]:
				continue
			else:
				graph[w_cur[i]] = graph.get(w_cur[i],[]) + [w_prev[i]]
				break
	alpha_order = []
	def dfs(graph, n, visited):
		nonlocal alpha_order
		if visited.get(n, False) is False:
			visited[n] = True
			for x in graph[n]:
				dfs(graph, x, visited)
			alpha_order.append(n)
		else:
			raise KeyError("Graph has CYCLES!")
	
	visited = {}
	for n in graph:
		try:
			dfs(graph, n, visited)
		except KeyError as exc:
			print(exc)
			break
	
	return alpha_order
			
tests = [
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]		

tests = ["z", "x", "z"]

print(alien_dictionary(tests))
		
				
		
