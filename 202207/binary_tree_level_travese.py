class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def traverse(root):
	levels = {}
	
	def recur(root, w=0):
		nonlocal levels
		if root is None:
			return
		else:
			levels[w] = levels.get(w, []) + [root.data]
			recur(root.left, w-1)
			
			recur(root.right, w+1)
			
	recur(root)
	path = []
	widths = list(levels.keys())
	widths.sort()
	for w in widths:
		path.append(levels[w])
	return path
	
root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

print(traverse(root))


root = Node(3)
root.left = Node(9)
root.left.left = Node(4)
root.left.right = Node(0)
root.right = Node(8)
root.right.left = Node(1)
root.right.right = Node(7)

print(traverse(root))
