def next_highest(num):
	
	#process from right to left
	num_list = list(str(num))
	prev = None
	index = None
	for i in range(len(num)):
		j = len(num) - i - 1
		if prev is not None and int(num_list[j]) < prev:
			index = j
			break
		prev = int(num_list[j])
	if index is None:
		return None
		
	d = -1
	shortest_index = -1
	for i in range(index+1, len(num)):
		if d == -1 and int(num_list[i]) > int(num_list[index]) :
			d = int(num_list[i]) - int(num_list[index])
			short_index = i
		else:
			dt = int(num_list[i]) - int(num_list[index])
			if dt < d:
				d = dt
				short_index = i
	
	num_list[index], num_list[short_index] = num_list[short_index], num_list[index]
	slice_to_sort = num_list[index+1:]
	slice_to_sort.sort()
	final_list = num_list[:index+1]  + slice_to_sort
	return final_list	
		
		
tests = [
	'123',
	'1001',
	'6789',
	'1111',
	'1011'
]

for t in tests:
	print(f'{t} : {next_highest(t)}')
	
