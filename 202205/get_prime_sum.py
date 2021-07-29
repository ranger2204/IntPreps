def get_prime_sum(num):
	def isprime(v):
		for i in range(2, v//2 + 1):
			if v%i == 0:
				return False
		return True
		
	def get_all_primes_till(num):
		primes = {}
		for i in range(2, num):
			if isprime(i):
				primes[i] = True
		return primes	
		
	primes = get_all_primes_till(num)
	
	for n in primes:
		d = num - n
		if d in primes:
			return (n, d)
		
	
	
tests = [
	100,
	102,

	98,
	4
]

for t in tests:
	p = get_prime_sum(t)
	print(f'{t} : {p}')
