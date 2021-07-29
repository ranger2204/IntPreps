def get_spread_sheet_col(num):
	max_value = 26
	alphas = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
	code_to_alpha = {i+1: alphas[i] for i in range(26)}
	
	col = []
	while num > 0:
		if num <= max_value:
			col.append(code_to_alpha[num])
			break
			
		d = num // max_value
		r = num - max_value * d
		if d != 0:
			col.append(code_to_alpha[d])
		
		num = r
			
	return ''.join(col)
	
	
tests = [
	1,
	26,
	27,
	28
]

for t in tests:
	print("{} : {}".format(t, get_spread_sheet_col(t)))
