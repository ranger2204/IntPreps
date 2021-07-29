def palindrome_check(num: int) -> bool:
	def count_digits(num: int) -> int:
		count = 0
		while num > 0:
			num = num // 10
			count += 1
		return count
	
	def extract_digit(num, p=0):
		if p == 0:
			return num%10
		else:
			return num//(10**p)	
	
	digit_count = count_digits(num)
#	print(digit_count)
	while digit_count > 0:
		#first
		f = extract_digit(num, digit_count-1)
		#last
		l = extract_digit(num, 0)
#		print(f, l)
		if f == l:
			num = num%(10**(digit_count-1))
			num = num/10
			digit_count -= 2
		else:
			return False
	return True
	
	
tests = [
	101,
	121,
	122,
	11,
	1
]
		
		
for t in tests:
	c = palindrome_check(t)
	print(f'{t} : {c}')
