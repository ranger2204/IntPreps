def min_hop_reach(hops):
	min_hops_so_far = float('inf')
	hop_path = []
	
	def hop_along(hops, k, no, path=[]):
		nonlocal min_hops_so_far, hop_path
		if k == len(hops) - 1:
			if min_hops_so_far >= no:
				hop_path = path + [k]
				min_hops_so_far = no
			
		elif k >= len(hops):
			return
		else:
			reach = hops[k]
			for i in range(1, reach+1):
				hop_along(hops, k+i, no+1, path+[k])
	
	hop_along(hops, 0, 0, [])
	print(hop_path)
	return min_hops_so_far
	
	
tests = [
	[1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
]

for t in tests:
	print(min_hop_reach(t))
