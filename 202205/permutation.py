
def permute(lst):
	if len(lst) <= 1:
		return [lst]
	else:
	
		perms = []
		for i in range(len(lst)):
			new_list = lst[0:i] + lst[i+1:]
			part_result = permute(new_list)
			result = [[lst[i]] + r for r in part_result]
			perms += result
			

		return perms


tests = [
	[1,0],
	[1,2,3]
]

for t in tests:

	perms = permute(t)
	print(f'{t}')
	for c in perms:
		print(f'{c}')
