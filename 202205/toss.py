import random

def toss_unbiased():
	v = random.randint(1, 100)
	if v%2 == 0:
		return 'H'
	return 'T'
	
print(toss_unbiased())
