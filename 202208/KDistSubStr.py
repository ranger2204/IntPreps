def find_sub_string(s):
	lookup = {}
	start = None
	sub_str = ""
	max_so_far = 0
	for i,c in enumerate(s):
		if start is None:
			start = i
			lookup[c] = 1
		else:
			lookup[c] = lookup.get(c, 0) + 1
			while len(lookup) > 2:
				l = i - start
				if l > max_so_far:
					max_so_far = l
					sub_str = s[start: i]
				
				lookup[s[start]] -= 1
				if lookup[s[start]] == 0:
					del lookup[s[start]]
				start = start + 1
				
	if (len(s)-start) > max_so_far:
		sub_str = s[start:]	
	return sub_str
	
	
tests = [
	"ecebaaab",
	"ccaabbb"
]

for t in tests:
	print(t, find_sub_string(t))
