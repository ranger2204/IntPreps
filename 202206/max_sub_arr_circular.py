def find_max_sub_arry(arr):
	
	def kadanes(arr):
		max_so_far = 0
		max_end_here = 0
		
		for c in arr:
			max_end_here = c + max_end_here
			if max_so_far < max_end_here:
				max_so_far = max_end_here
			if max_end_here < 0:
				max_end_here = 0
		return max_so_far
		
	
	total_sum = sum(arr)
	
	pos_max = kadanes(arr)
	
	for i in range(len(arr)):
		arr[i] = -1*arr[i]
		
	neg_max = kadanes(arr)
	neg_total_sum = sum(arr)
	
	return max(total_sum + neg_max, pos_max)
	

tests = [
	[2, 1, -5, 4, -3, 1, -3, 4, -1],
	[-3, 1, -3, 4, -1, 2, 1, -5, 4]
]


for t in tests:
	print(find_max_sub_arry(t))
