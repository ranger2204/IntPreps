

def max_distinct_cont_array(nums):
	lookup = {}
	l = -1
	r = 0
	max_len = 0
	while r < len(nums):
		d = nums[r]
		if l == -1:
			l = 0
		else:
			if lookup.get(d, 0) >= 1:
				new_len = r - l
				max_len = max(new_len, max_len)
				
				while l < r:
					prev = nums[l]
					lookup[prev] -= 1
					l += 1
					if d == prev:
						break
		lookup[d] = lookup.get(d, 0) + 1
		r += 1
	
	new_len = r - l
	max_len = max(max_len, new_len)
	
	return max_len
	
	


tests = [
	[5, 1, 3, 5, 2, 3, 4, 1],
	
	[5, 1, 3, 5, 2, 3, 4, 5]
]	


for t in tests:
	r = max_distinct_cont_array(t)
	print(r)
					
