class Solution:
	def find_min_attempts(self, eggs, floors):
		memo = {}
		
		def recur(eggs, floors):
			nonlocal memo
			if eggs == 1:
				return floors
			if floors == 0 or floors == 1:
				return floors
			min_so_far = float('inf')
			
			if eggs in memo:
				if floors in memo[eggs]:
					return 1 + memo[eggs][floors]
			
			for f in range(1, floors+1):
				cur_min = max(
						recur(eggs, floors-f), 	#egg not broken at floor f
						recur(eggs-1, f-1)		#egg broken at floor f
					)
					
				min_so_far = min(cur_min, min_so_far)
			
			if eggs in memo:
				memo[eggs][floors] = min_so_far
			else:
				memo[eggs] = {
					floors: min_so_far
				}
				
			print(eggs, floors, min_so_far)
			return 1+min_so_far
			
		result = recur(eggs, floors)
		return result
		

tests = [
	{
		'eggs': 2,
		'floors': 10
	},
]

for t in tests:
	print(Solution().find_min_attempts(**t))

