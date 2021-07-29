class Node:
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None
		

def zigzag(root):
	q = []
	q.append(root)
	i = 0
	result = []
	while len(q) != 0:
		l = len(q)
		t_result = []
		for j in range(l):
			n = q.pop(0)
			t_result.append(n.data)
			if n.left is not None:
				q.append(n.left)
			if n.right is not None:
				q.append(n.right)
				
		if i%2 != 0:
			result += t_result[::-1]
		else:
			result += t_result
		i += 1
				
	print(result)
	return result
	



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)


zigzag(root)
