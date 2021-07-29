class Quack:
	
	def __init__(self):
		self.s1 = []
		self.s2 = []
		self.s3 = []
		self.sz = 0
	
	
	def push(self, item):
		self.s1.append(item)
		self.s2.append(item)
		self.sz += 1
	
	def clear_stacks(self):
		self.s1 = []
		self.s2 = []
		self.s3 = []
	
	def pop(self):
		item = None
		if self.sz > 0:
			item = self.s1.pop(-1)
			if len(self.s2) > 0:
				self.s2.pop(-1)
			self.sz -= 1
			if self.sz == 0:	
				self.clear_stacks()
		else:
			raise ValueError("Empty Quack!")
		return item
		
		
	def pull(self):
		item = None
		if self.sz > 0:
			if len(self.s3) == 0:
				while len(self.s2) > 0:
					item = self.s2.pop(-1)
					self.s3.append(item)
			item = self.s3.pop(-1)
			self.sz -= 1
			if self.sz == 0:	
				self.clear_stacks()
		else:
			raise ValueError("Empty Quack!")
		return item
		
	def __repr__(self):
		return """
		Size : {}
		S1: {}
		S2: {}
		S3: {}
		""".format(self.sz, self.s1, self.s2, self.s3)
		


q = Quack()
q.push(1)
q.push(2)
q.push(3)

print(q)
print(q.pop())
print(q.pull())
print(q)
q.push(4)
print(q)
print(q.pull())
print(q.pull())
q.push(5)
print(q.pull())
print(q)

