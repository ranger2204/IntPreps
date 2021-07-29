import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)

class LFUCache:
	def __init__(self, n):
		self.max_N = n
		self.data = {}
		self.freqs = {}
		self.min_freq = None
		
	def add(self, k, v):
		cur_len = len(self.data)
		diff = self.max_N - cur_len
		
			
		if diff >= 1:
			self.data[k] = {
				'value': k,
				'freq': 1
			}
			freq = self.data[k]['freq']
			
			if freq not in self.freqs:
				self.freqs[freq] = {}
			self.freqs[freq][k] = True
			if self.min_freq is None or self.min_freq > 1:
				self.min_freq = freq
			
		else:
			min_freq_k = list(self.freqs[self.min_freq].keys())[0]
			print("Removing : {}".format(min_freq_k))
			del self.data[min_freq_k]
			del self.freqs[self.min_freq][min_freq_k]
			if len(self.freqs[self.min_freq]) == 0:
				self.min_freq += 1
			self.add(k, v)
			
	def get(self, k):
		if k in self.data:
			freq = self.data[k]['freq']
			self.data[k]['freq'] += 1
			del self.freqs[freq][k]
			if len(self.freqs[freq]) == 0:
				if freq == self.min_freq:
					self.min_freq += 1
			if freq+1 not in self.freqs:
				self.freqs[freq+1] = {}
				
			self.freqs[freq+1][k] = True
			return self.data[k]['value']
		return None
		
		
cache = LFUCache(3)
cache.add(1, 'a')
cache.add(2, 'b')
cache.add(3, 'c')
cache.add(4, 'd')
cache.add(5, 'e')
cache.add(6, 'f')
cache.get(4)
cache.get(6)
cache.add(7,'g')
cache.add(8, 'h')

		
