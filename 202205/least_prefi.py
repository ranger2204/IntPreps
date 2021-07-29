class Node:
	def __init__(self, val):
		self.val = 'root'
		self.links = {}
		self.count = 1
		
		
		


def create_trie(root, words):

	for w in words:
		cur = root
		for c in w:
			if c not in cur.links:
				cur.links[c] = Node(c)
			else:
				cur.links[c].count += 1
				
			cur = cur.links[c]
	return root


def get_least_pref(root, word):
	cur = root
	pref = []
	for c in word:
		pref += [c]
		if cur.links[c].count == 1:
			return pref
		else:
			cur = cur.links[c]
	return pref
	
	

words = [
	'dog', 'cat', 'apple', 'apricot', 'fish'
]


root = Node('')
root = create_trie(root, words)

for w in words:
	pre = get_least_pref(root, w)
	print(f'{w} : {pre}')
