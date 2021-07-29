def compare_sentences(a, b, repo):
	wa = a.split(' ')
	wb = b.split(' ')
	
	for i, v in enumerate(wa):
		w = wb[i]
		if v != w:
			if repo.get(v, '') == w or repo.get(w, '') == v:
				continue
			else:
				return False
	return True
	
	
repo = {
	'consume': 'eat',
	'big': 'large',
}



tests = [
	[
		"He wants to eat food",
		"He wants to consume food"
	],
	[
		"He wants to consume food",
		"He wants to eat food"
	],
	[
		"He wants to eat food",
		"He wants to bite food"
	]
]

for t in tests:
	c = compare_sentences(*t, repo=repo)
	print(f'{t} : {c}')
	
