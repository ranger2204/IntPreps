def find_match_indices(s, p):
	v = 1
	char_hash = {}
	result = []
	for c in s:
		if c not in char_hash:
			char_hash[c] = v
			v += 1    

	pat_hash = 0
	for c in p:
		pat_hash = pat_hash*10 + char_hash[c]

	str_hashes = [0 for c in s]
	for i, c in enumerate(s):
		if i <= len(p) - 1:
			if i == 0:
				str_hashes[i] = char_hash[c]
			else:
				str_hashes[i] = str_hashes[i-1]*10 + char_hash[c]  

		else:
			str_hashes[i] = 10*(str_hashes[i-1] - char_hash[s[i-len(p)]]*(10**(len(p)-1))) + char_hash[c]

			if str_hashes[i] == pat_hash:
				s_i = i - len(p) + 1
				m = 0
				for i in range(len(p)):
					if s[s_i+i] == p[i]:
						m += 1
				if m == len(p):
					result.append(s_i)
	print(char_hash)
	print(pat_hash)
	print(str_hashes)
	return result
		
	
test = [
	{
		's': 'abcdeccdecde',
		'p': 'cde'
	}
]

for t in test:
	print(find_match_indices(**t))
	
