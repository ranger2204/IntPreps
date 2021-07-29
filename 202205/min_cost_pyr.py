def find_min_cost_pyramid(arr):
	min_so_far = float('inf')
	
	for i,v in enumerate(arr):
		total_cost = 0
		prev = v
		exp = -1
#		print(f'{i}')
		for j in range(i+1, len(arr)):
			exp = prev - 1
#			print(f'{exp} - {arr[j]}')
			if exp < 0:
				break
			if exp <= arr[j]:
				total_cost += abs(arr[j] - exp)
			else:
				exp = -1
				break
			prev = exp
			
		if exp < 0:
			continue
#		print(f'R {total_cost}')
		next = v
		for j in range(1, i+1):
			k = i - j
			exp = next - 1
#			print(f'{exp} - {arr[k]}')
			if exp < 0:
				break
			if exp <= arr[k]:
				total_cost += abs(arr[k] - exp)
			else:
				exp = -1
				break
			next = exp
			
		if exp < 0:
			continue
			
#		print(f'L {total_cost}')
	
		min_so_far = min(min_so_far, total_cost)
#		if min_so_far == total_cost:
#		print(f'min : {i} : {total_cost}')
		
	return min_so_far
	


tests = [
	[1,1,3,3,2,1]
]

for t in tests:
	cost = find_min_cost_pyramid(t)
	print(f'{t} : {cost}')
		
		
		
