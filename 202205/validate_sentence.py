class Validator:
	
	alphas = set(list('abcdefghijklmnopqrstuvwxyz'))
	seps = set(list(',;:'))
	terms = set(list('.?$!'))

	@staticmethod
	def is_upper(char):
		if char == char.upper():
			return True
		return False
	
	@staticmethod
	def is_low_alpha(char):
		return char in Validator.alphas
	
	@staticmethod
	def is_valid_low_alpha_syms(char):
		return char in Validator.alphas or char in Validator.seps or char in Validator.terms	
		
	@staticmethod
	def validate(sent):
		space_count = 0
		word_count  =0
		for i, c in enumerate(sent):
			if i == 0:
				if not Validator.is_upper(c) or not c.isalpha():
					return f'Doesnt start with caps! @{i} {c}'
				continue
				
			if c.isspace():
				if space_count > 0:
					return f"Multiple spaces! @{i}"
				space_count += 1
				word_count += 1
				continue
			else:
				space_count = 0
			
				
						
			if i == len(sent) - 1:
				if c not in Validator.terms:
					return f"Non terminal @{i} {c}"
				if not Validator.is_low_alpha(sent[i-1]):
					return f"Non alpha pre terminal @{i} {c}"
				continue
			
			if not Validator.is_valid_low_alpha_syms(c):
				
				return f"Non low alphas or symbols @{i} {c}"
			
		
		return True
		
		
tests = [
	'I am ok.',
	'I\'m  not ok',
	'Really?'

]

for s in tests:
	v = Validator.validate(s)
	print(f"{s} : {v}")
