combs = []

def generate_combs(nums, cur, i=0):
	if i >= len(nums):
		if len(cur) > 0:
			combs.append(cur)
	else:
		generate_combs(nums, cur+[nums[i]], i+1)
		generate_combs(nums, cur, i+1)
		
		

nums = [7**i for i in range(3)]
generate_combs(nums, [], i=0)
sums = [sum(c) for c in combs]
sums.sort()
print(sums)
