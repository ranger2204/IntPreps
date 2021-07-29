class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		

def rearrange(head):
	prev = None
	cur = head
	while cur is not None:
		if prev is None:
			prev = cur

		else:
			if cur.next is not None:
				next_to_be = cur.next.next
				new_cur = cur.next
				prev.next = new_cur
				new_cur.next = cur
				cur.next = next_to_be
		prev = cur
		cur = cur.next
	
	return head
	
	
root = Node(1)
root.next = Node(2)
root.next.next = Node(3)
root.next.next.next = Node(4)
#root.next.next.next.next = Node(5)


head = rearrange(root)
while head is not None:
	print(head.data)
	head = head.next
	
