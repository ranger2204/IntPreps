class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		
def get_max_path(root):
	
	
	def recur(root, par):
		if root is None:
			return 1
		else:
			if par is None or par.val + 1 != root.val:
				return max(recur(root.left, root), recur(root.right, root))
			else:
				return 1 + max(recur(root.left, root), recur(root.right, root))
				
	return recur(root, None)
	
	
root = Node(5)
root.left = Node(8)
root.left.left = Node(9)
root.left.left.left = Node(6)
root.right = Node(11)

root.right.right = Node(10)
root.right.right.left = Node(15)


print(get_max_path(root))
