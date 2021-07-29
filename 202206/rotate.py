def reverse(l, s, e):
	m = (e - s)// 2
	for i in range(m+1):
		l[s+i], l[e-i] = l[e-i], l[s+i]
		
def rotate(l, k):
	reverse(l, 0, k-1)
	reverse(l, k, len(l)-1)
	reverse(l, 0, len(l)-1)
	return l
	
	
tests = [
	[1,2,3,4,5,6]
]

for t in tests:
	print(rotate(t, 3))
