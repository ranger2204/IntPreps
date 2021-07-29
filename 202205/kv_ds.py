class Node:
	def __init__(self, value):
		self.value = value
		self.keys = {}
		self.max_key = None
		self.min_key = None

class KVDS:
	def __init__(self):
		self.data = {}
		self.keys = {}
		self.max_value = None
		self.min_value = None
		
	
	
	def plus(self, k):
		self.data[k] = self.data.get(k, 0) + 1
		prev = self.data[k] - 1
		cur = self.data[k]
		
		if prev in self.keys:
			if k in self.keys[prev]:
				del self.keys[prev][k]
			if prev == self.max_value:
				if len(self.keys[prev]) == 0:
					del self.keys[prev]
					self.max_value += 1
			if prev == self.min_value:
				if len(self.keys[prev]) == 0:
					self.min_value += 1
		
		if cur not in self.keys:
			self.keys[cur] = {
				k: True
			}
		else:
			self.keys[cur][k] = True
		
		self.init_min_max(cur)
		
		if cur > self.max_value:
			self.max_value = cur
	
	def get_max(self):
		return list(self.keys[self.max_value].keys())[0]
		
	def get_min(self):
		return list(self.keys[self.min_value].keys())[0]
		
	def init_min_max(self, cur):
		self.min_value = cur if self.min_value is None else self.min_value
		self.max_value = cur if self.max_value is None else self.max_value
		
	
	def minus(self, k):
		self.data[k] = self.data.get(k, 0) - 1
		prev = self.data[k] + 1
		cur = self.data[k]
		
		if prev in self.keys:
			if k in self.keys[prev]:
				del self.keys[prev][k]
			if prev == self.min_value:
				if len(self.keys[prev]) == 0:
					del self.keys[prev]
					self.min_value -= 1
			if prev == self.max_value:
				if len(self.keys[prev]) == 0:
					self.max_value -= 1
		
		if cur not in self.keys:
			self.keys[cur] = {
				k: True
			}
		else:
			self.keys[cur][k] = True
			
		if cur < self.min_value:
			self.min_value = cur
			
		self.init_min_max(cur)
		
		


kv = KVDS()
kv.plus(1)
kv.plus(2)
print(kv.keys)
print(kv.get_max())
print(kv.get_min())


kv.plus(2)
print(kv.keys)
print(kv.get_max())

kv.minus(1)
print(kv.keys)
print(kv.get_max())
print(kv.get_min())


kv.plus(2)
print(kv.keys)
print(kv.get_max())
print(kv.get_min())


kv.plus(3)
kv.plus(3)
kv.plus(3)
kv.plus(3)
print(kv.keys)
print(kv.get_max())
print(kv.get_min())

kv.minus(2)
kv.minus(2)
kv.minus(2)
kv.minus(2)
print(kv.keys)
print(kv.get_max())
print(kv.get_min())


		
		
