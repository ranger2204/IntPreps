class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		
def preorder(root):
	if root is None:
		return
	else:
		print(root.data)
		preorder(root.left)
		preorder(root.right)

def invert_tree(root):
	if root is None:
		return None
	else:
		new_node = Node(root.data)
		new_node.left = invert_tree(root.right)
		new_node.right = invert_tree(root.left)
		return new_node
		


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

#		1
#	2		3
#4		5

#		1
#	3 		2
#		5	 	4

preorder(root)
root = invert_tree(root)
preorder(root)
