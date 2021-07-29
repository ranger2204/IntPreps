def merge_intervals(int_list):
	
	int_list.sort(key=lambda x: x[0])
	par = None
	i = 0
	out_list = []
	while i < len(int_list):
		cur = int_list[i]
		if par is None:
			par = cur
		else:
			if cur[0] >= par[0] and cur[1] <= par[1]:
				par[0] = min(par[0], cur[0])
				par[1] = max(par[1], cur[1])
			else:
				out_list.append(par)
				par = cur
			
		i += 1
	if par is not None:
		out_list.append(par)
		
	return out_list
	
	
tests = [
	[
		[1, 3], [4, 5], [6, 8], [20, 25]
	]
]


for t in tests:
	print(merge_intervals(t))
