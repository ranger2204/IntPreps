def split_wo_break(s, k):
	words = s.split(' ')
		
	result = []
	i = 0
	cur_set = []
	cur_len = 0
	while i < len(words):
		w = words[i]
		w_len = len(w)
		cur_len += w_len
		if cur_len <= (k - len(cur_set) + 1):
			cur_set.append(w)
		else:
			result += [' '.join(cur_set)]
			cur_set = [w]
			cur_len = w_len
		i += 1
	
	if len(cur_set) > 0:
		result += [' '.join(cur_set)]
		
	return result
	
	
test = [
	"the quick brown fox jumps over the lazy dog"
]

for t in test:
	print(split_wo_break(t, 10))
	
