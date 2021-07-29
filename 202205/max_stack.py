class MaxStack:
	def __init__(self):
		self.data = []
		self.max_val = None
		
	def push(self, val):
		
		if self.max_val is None:
			self.max_val = val
			self.data.append(val)

		elif self.max_val < val:
			self.data.append(2*val - self.max_val)
			self.max_val = val
			
		
			
	def pop(self):
		try:
			val = self.data.pop(-1)
			if val > self.max_val:
				real_val = self.max_val
				self.max_val = 2*self.max_val - val
				return real_val
			if val == self.max_val:
				self.max_val = None
				
			return val
		except IndexError as exc:
			print("Stack EMPTY!")
		
	def get_max(self):
		return self.max_val
		
		

ms = MaxStack()
ms.push(1)
ms.push(2)
ms.push(30)

print(ms.get_max())
ms.pop()
print(ms.get_max())
ms.pop()
print(ms.get_max())
ms.pop()
print(ms.get_max())
ms.pop()
print(ms.get_max())

