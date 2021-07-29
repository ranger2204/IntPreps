class Solution:
	def get_no_cc(self, n, edges):
		parent = {}
		unq_parent = {}
		for i in range(n):
			parent[i] = i
		
		def get_parent(i):
			nonlocal parent
			if parent[i] == i:
				return i
			else:
				p = get_parent(parent[i])
				parent[i] = p
				return p
		
		for edge in edges:
			s, e = edge
			p_s = get_parent(s)
			p_e = get_parent(e)
			
			if p_s != p_e:
				parent[p_e] = p_s
		
		for k in parent:
			p = get_parent(k)
			unq_parent[p] = True
		return len(unq_parent)
		
tests = [
	{
		'n': 5,
		'edges': [[0, 1], [1, 2], [3,4]]
	},
	{
		'n': 5,
		'edges': [[0,1],[1,2],[2,3],[3,4]]
	
	}
]

for t in tests:
	print(Solution().get_no_cc(**t))
				
