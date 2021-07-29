import logging

logging.basicConfig(level=logging.INFO)

class Node:
	def __init__(self, prev, k, v):
		self.prev = prev
		self.next = None
		self.key = k
		self.value = v
		
	def __repr__(self):
		return "<K : {} V : {}>".format(self.key, self.value)

class LRUCache:
	def __init__(self, size=10):
		self.max_size = size
		self.cur_size = 0 
		self.lookup = {}
		self.head = None
		self.tail = None
	
	def add_data(self, k, v):
		try:
			node = self.lookup[k]
			raise KeyError("Key : {} exists!!".format(k))
		except KeyError:
			if self.cur_size >= self.max_size:
				node_to_del = self.tail
				self.tail = self.tail.prev
				self.tail.next = None
				logging.info('Removing : {}'.format(node_to_del))
				del self.lookup[node_to_del.key]
				self.cur_size -= 1
			
			node = Node(None, k, v)
			node.next = self.head
			self.lookup[k] = node
			
			if self.head is not None:
				self.head.prev = node
			
			self.head = node
			
			if self.tail is None:
				self.tail = node
			self.cur_size += 1
			
			
	def get_data(self, k):
		if k not in self.lookup:
			raise KeyError("Key {} not in cache!")
		node = self.lookup[k]
		if self.head != node:
			node.prev.next = node.next
			node.next.prev = node.prev
		
		node.next = self.head
		self.head.prev = node
		self.head = node
		
		return node.value
		
		
	def show(self):
		cur = self.head
		while cur is not None:
			print(cur, end='')
			cur = cur.next
		print()
		
		
		
cache = LRUCache(3)
cache.add_data('a', 1)
cache.add_data('b', 2)
cache.add_data('c', 3)
cache.show()

cache.add_data('d', 4)
cache.show()
cache.get_data('c')
cache.show()
cache.add_data('a',1)
cache.show()

