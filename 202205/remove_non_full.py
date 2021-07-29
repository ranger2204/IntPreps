class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		



def remove_nodes_with_one_child(root):
	if root is None:
		return None
	else:
		if root.left is None and root.right is None:
			return root
		else:
			
			if root.left is None:
				print(f'Removing : {root.value}')
				root.right = remove_nodes_with_one_child(root.right)
				return root.right
			elif root.right is None:
				print(f'Removing : {root.value}')
				root.left = remove_nodes_with_one_child(root.left)
				return root.left
			else:
				root.left = remove_nodes_with_one_child(root.left)
				root.right = remove_nodes_with_one_child(root.right)
				return root


root = Node(0)
root.left = Node(1)
root.right = Node(2)
root.left.left = Node(3)
root.right.right = Node(4)
root.left.left.right = Node(5)
root.right.right.left = Node(6)
root.right.right.right = Node(7)

def dfs(root):
	if root is None:
		return None
	else:
		print(f'{root.value}')
		dfs(root.left)
		dfs(root.right)
	

root = remove_nodes_with_one_child(root)
dfs(root)
