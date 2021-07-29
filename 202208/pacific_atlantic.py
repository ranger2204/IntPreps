from collections import List

class Solution:
	def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
		
		m, n = len(heights), len(heights[0])

		dx = [0, 0, -1, 1]
		dy = [1, -1, 0, 0]
		
		def get_key(x, y):
			return "{}_{}".format(x,y)
		
		def move(heights, x, y, marked):
			nonlocal m
			nonlocal n
			r = get_key(x, y)
			if marked.get(r, False):
				return
			marked[r] = True
			for i in range(4):
				nx, ny = x+dx[i], y+dy[i]
				if nx >=0 and ny >= 0 and nx < m and ny < n and heights[nx][ny] >= heights[x][y]:
					move(heights, nx, ny, marked)
					
		seen_P = {}
		seen_A = {}
		for i in range(n):
			move(heights, 0, i, seen_P)
			move(heights, m-1, i, seen_A)

		for i in range(m):
			move(heights, i, 0, seen_P)
			move(heights, i, n-1, seen_A)



		result = []
		for i in range(m):
			for j in range(n):
				r = get_key(i, j)
				if seen_P.get(r, False) and seen_A.get(r, False):
					result.append([i,j])
					
		return result