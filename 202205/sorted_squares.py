def sort_squares(nums):
	neg_end_index = -1
	for i, v in enumerate(nums):
		if v < 0:
			neg_last_index = i
		else:
			break
	
	negs = nums[0:neg_last_index+1]
	
	a = [n**2 for n in negs]
	b = [n**2 for n in nums[neg_last_index+1:]]
	
	print(a, b)
	i = j = 0
	c = []
	while i < len(a) and j < len(b):
		if a[i] < b[j]:
			c.append(a[i])
			i += 1
		else:
			c.append(b[j])
			j += 1
			
	if i >= len(a):
		c += b[j:]
	if j >= len(b):
		c += a[i:]
	return c


tests = [
	[-9, -2, 0, 2, 3]
]

for t in tests:
	print(sort_squares(t))
