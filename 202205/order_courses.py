def find_course_orders(course_with_pres):
	
	completed = {}
	visited = {}
	
	def dfs(cur_course, course_with_pres, completed, visited):
		if cur_course in completed:
			return
		else:
			visited[cur_course] = True
			for c in course_with_pres.get(cur_course, []):
				dfs(c, course_with_pres, completed, visited)
			completed[cur_course] = True
			
	for c in course_with_pres:
		if c not in visited:
			dfs(c, course_with_pres, completed, visited)
	
	return list(completed.keys())
	
tests = [
	{'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}
]

for t in tests:
	print(find_course_orders(t))
	
	
