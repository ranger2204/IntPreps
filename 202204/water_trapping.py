class Solution:
	def find_max_water_trapped(self, arr):
		left_max = []
		right_max = []
		
		for i, v in enumerate(arr):
			if i == 0:
				left_max.append(v)
			else:
				left_max.append(max(v, left_max[i-1]))
			j = len(arr) - i - 1
			w = arr[j]
			if j == len(arr) - 1:
				right_max.append(w)
			else:
				right_max.append(max(w, right_max[i-1]))
		
		right_max = right_max[::-1]
		max_water = 0
		for i in range(len(arr)):
			max_height = min(left_max[i], right_max[i])
			max_water += (max_height - arr[i])
			
		return max_water
	

tests = [
	[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
]

for t in tests:
	print(Solution().find_max_water_trapped(t))
	
#0 1 0 2 1 0 1 3 2 1 2 1	
#0 1 1 2 2 2 2 3 3 3 3 3
#3 3 3 3 3 3 3 3 2 2 2 1	
#0 0 1 0 1 2 1 0 0 1 0 0
