def get_nos_greater(nums, key):
	l = 0
	r = len(nums) - 1
	m = -1
	while l <= r:
		m = (l + r) // 2
		if nums[m] >= key:
			r = m - 1
		else:
			l = m + 1
#	print(key, l, r)
#	k = min(l, r)
	return len(nums) - r - 1
	
	
tests = [
	[1, 2, 3, 4, 5, 6]
]


for t in tests:
	for c in t:
		nos = get_nos_greater(t, c)
		print(f"{t} >= {c} : {nos}")
