def get_lowest_missing(nums):	
	i = 0
	l = len(nums)
	while i < l:
		c = nums[i]
		if c <= 0:
			i += 1
			continue
			
		if c-1 != i and (c-1) < l:
			nums[c-1], nums[i] = c, nums[c-1]
			continue
		i += 1
	
	for i, v in enumerate(nums):
		if v <= 0 or v-1 != i:
			return i+1
	return l
	
	
tests = [
	[1,2,0],
	[3, 4, -1, 1]
]


for t in tests:
	print(get_lowest_missing(t))
