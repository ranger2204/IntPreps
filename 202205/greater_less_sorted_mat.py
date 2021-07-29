def find_greater(row, k):
	l = 0
	r = len(row) - 1
	
	while l <= r:
		m = (l + r) // 2
		if row[m] >= k:
			r = m - 1
		else:
			l = m + 1
	return len(row) - r - 1

def gt_lt(mat, p, q):
	output = 0
	
	l = mat[p[0]][p[1]]
	h = mat[q[0]][q[1]]
	
	m = len(mat)
	n = len(mat[0])
	for row in mat:
		k = find_greater(row, l)
		output += (n - k)
		k = find_greater(row, h)
		output += k
	
	print(output)
	return output
	
	
mat = [
	[1, 3, 7, 10, 15, 20],
	[2, 6, 9, 14, 22, 25],
	[3, 8, 10, 15, 25, 30],
	[10, 11, 12, 23, 30, 35],
	[20, 25, 30, 35, 40, 45]
]

gt_lt(mat, (1,1), (4,3))
