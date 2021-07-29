def pow(x, y):
	if y == 0:
		return 1
	else:
		py = y
		if y < 0:
			py =  -1*py
			
		part_result = pow(x, py//2)
		if y%2 == 0:
			result = part_result * part_result
		else:
			result = x * part_result * part_result
		
		if py != y:
			result = 1/float(result)
		return result	
		

		
tests = [
	[2,3],
	[2, -3]
]

for t in tests:
	print(t, pow(t[0], t[1]))
