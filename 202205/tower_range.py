def min_range(listeners, towers):
	i = j = 0
	prev_tower = -1
	max_so_far = 0
	output = []
	while i < len(listeners) and j < len(towers):
		l = listeners[i]
		t = towers[j]
		
		if l < t:
			output.append([l, 'l'])
			i += 1
		else:
			output.append([t, 't'])
			j += 1
	
	if i == len(listeners):
		output += [[t, 't'] for t in towers[j:]]
	if j == len(towers):
		output += [[l, 'l'] for l in listeners[i:]]
	
#	print(output)
	
	left_tower = []
	right_tower = []
	
	last_tower = None
	for c in output:
		v, t = c
		if t == 't':
			left_tower.append(v)
			last_tower = v
		else:
			left_tower.append(last_tower)
	
	last_tower = None
	for i in range(len(output)):
		j = len(output) - i - 1
		v, t = output[j]
		if t == 't':
			right_tower.append(v)
			last_tower = v
		else:
			right_tower.append(last_tower)
	
	right_tower = right_tower[::-1]
	
#	print(left_tower)
#	print(right_tower)
	
	max_ranges = []
	for i, v in enumerate(output):
		c,t = v
		if t == 't':
			continue
			
		min_local = float('inf')
		if left_tower[i] is not None:
			min_local = abs(c - left_tower[i])
		
		if right_tower[i] is not None:
			min_local = min(min_local, abs(c-right_tower[i]))
		
		max_ranges.append(min_local)
		
	print(max_ranges)
	return max(max_ranges)
	


tests = [
	{
		'listeners': [1, 5, 11, 20],
		'towers': [4, 8, 15]
	}
]
				
for t in tests:
	r = min_range(**t)
	print(r)
		
