def bomb_enemies(grid):
	m,n = len(grid), len(grid[0])
	cols = [0 for _ in range(n)]
	
	max_bombed = 0
	
	def scan_along_row(grid, i, j):
		bombed = 0
		while j < n and grid[i][j] != 'W':
			if grid[i][j] == 'E': bombed += 1
			j += 1
		return bombed
	
	def scan_along_col(grid, i, j):
		bombed = 0
		while i < m and grid[i][j] != 'W':
			if grid[i][j] == 'E': bombed += 1
			i += 1
		return bombed
				
	for i in range(m):
		for j in range(n):
			if j == 0 or grid[i][j-1] == 'W':
				row = scan_along_row(grid, i, j)
			
			if i == 0 or grid[i-1][j] == 'W':
				cols[j] = scan_along_col(grid, i, j)
			
			
			if grid[i][j] == 'O':
				max_bombed = max(max_bombed, row+cols[j])
	return max_bombed

grid = [
		list('OEOO'),
		list('EOWE'),
		list('OWOO')
	]
	
print(bomb_enemies(grid))
