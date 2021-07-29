def max_profit(prices):
	stack = []
	profit_so_far = 0
	for i, p in enumerate(prices):
		if len(stack) == 0:
			stack.append(p)
		else:
			prev = prices[i-1]
			if p <= prev:
				#pop stack
				if len(stack) > 0:
					s = stack.pop(-1)
					profit_so_far += (prev-s)	
				
				stack.append(p)
	if len(stack) > 0:
		prev = prices[len(prices)-1]
		s = stack.pop(-1)
		profit_so_far += (prev - s)
		
	return profit_so_far
	



tests = [
	[100, 180, 260, 310, 40, 535, 695]
]

for t in tests:
	print(max_profit(t))
		
					
				
