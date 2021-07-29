class Solution:
	
	def create_graph(self, ranks_list):
		graph = {}
		for ranks in ranks_list:
			for i, v in enumerate(ranks):
				if i != 0:
					prev = ranks[i-1]
					graph[prev] = graph.get(prev, []) + [v]
					
		return graph
	
	def dfs(self, graph):

		def recur(graph, cur_node, marked={}, ordered=[]):
			if marked.get(cur_node, 0) != 0:
				return
			else:
				marked[cur_node] = 1
				for n in graph.get(cur_node, []):
					recur(graph, n, marked, ordered)
				ordered.append(cur_node)
		marked = {}
		ordered = []	
		for n in graph:
			recur(graph, n, marked, ordered)
		return ordered[::-1]
				
	def find_interleaved(self, ranks_list):
		graph = self.create_graph(ranks_list)
		ordered_nodes = self.dfs(graph)
		print(ordered_nodes)
		
		
		
if __name__ == "__main__":
	tests = [
		[
			[1, 7, 3], [2, 1, 6, 7, 9], [3, 9, 5]
		]
	]
	
	for t in tests:
		Solution().find_interleaved(t)
		
		
