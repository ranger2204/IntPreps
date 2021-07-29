class Node:
	def __init__(self, char):
		self.char = char
		self.end = 0
		self.links = {}
		


def create_trie(root, words):
	for w in words:
		cur = root		
		for c in w:
			if c not in cur.links:
				cur.links[c] = Node(c)
			cur = cur.links[c]
		cur.end += 1
	return root


def get_words(s, root):
	cur = root
	result = []
	inter = []
	for c in s:
		if c in cur.links:
			
			cur = cur.links[c]
		else:	
			#go back up to root
			cur = root
			if c not in links:
				return None
			cur = cur.links[c]
		inter.append(c)
		if cur.end > 0:
			result.append(''.join(inter))
			inter = []
			cur = root
	if cur.end > 0:
		result.append(''.join(inter))
	return result
	
	


words = [
'bed', 'bath', 'bedbath', 'and', 'beyond'
]
s = 'bedbathandbeyond'

r = Node('')
r = create_trie(r, words)
print(get_words(s, r))

