def find_max_depth(tree_str):
	max_depth = 0
	stack = []
	for c in tree_str:
		if c == '(':
			stack.append(c)
		elif c == ')':
			max_depth = max(max_depth, len(stack))
			stack.pop(-1)
	return max_depth-1
	

tests = [
	"((((00)0)0)0)",
	"((00)(00))",
	"(00)"
]

for t in tests:
	print(t, find_max_depth(t))
