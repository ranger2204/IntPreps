memo = {}

def get_no_ways(dices, faces, total):

	if total == 0 and dices == 0:
		return 1
	if dices == 0:
		return 0
	if total == 0:
		return 0
	
	if dices in memo:
		if total in memo[dices]:
			return memo[dices][total]
	else:
		memo[dices] = {}
		
	final = 0
	for i in range(1, faces+1):
		r = 1*get_no_ways(dices-1, faces, total-i)
		final += r
		
	memo[dices][total] = final
	return final
	
tests = [
	[3, 6, 7],
	[1, 6, 6]
]

for t in tests:
	ways = get_no_ways(*t)
	print(f'{t} : {ways}')
