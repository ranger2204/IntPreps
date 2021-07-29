def max_combination(nums):
	 
	 def sort(nums):
	 	
	 	for i in range(len(nums)):
	 		for j in range(i+1, len(nums)):
	 			if int(str(nums[i]) + str(nums[j])) < int(str(nums[j]) + str(nums[i])):
	 				nums[i], nums[j] = nums[j], nums[i]
	 	
	 	return nums
	 	
	 nums = sort(nums)
	 return ''.join(map(str, nums))
	 
tests = [
	[1,2,3,4],
	[10, 7, 76, 415]
	
]

for t in tests:
	c = max_combination(t)
	print("{} : {}".format(t, c))
