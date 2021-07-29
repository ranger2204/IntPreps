def get_next_prime():
	base_primes = [2, 3, 5, 7]
	
	def get_multiples(m, start=0, max_val=100):
		p = 0
		result = []	
		
		f = max(2, start//m)
		p = m*f
		while p <= max_val:
			result.append(p)
			f += 1
			p = m * f
			
		return result
		
	prev_start = 2
	end = 100
	marked = {}
	while True:
		for p in base_primes:
			result = get_multiples(p, prev_start, end)
		
			for r in result:
				marked[r] = True
		
		for n in range(prev_start, end):
			if n not in marked:
				base_primes.append(n)
				yield(n) 
		prev_start = end
		end += 100
		
prime = get_next_prime()
for i in range(1, 100):
	print(next(prime))
