class Node:
	def __init__(self, val):	
		self.val = val
		self.left = None
		self.right = None
		


def merge_trees(r1, r2):
	if r1 is None and r2 is None:
		return None:
	if r1 is None:
		return r2
	if r2 is None:
		return r1
	
	new_node = Node(r1.val+r2.val)
	new_node.left = merge_trees(r1.left, r2.left)
	new_node.right = merge_trees(r1.right, r2.right)
	
	return new_node
	
