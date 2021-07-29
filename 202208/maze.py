def check_reachable(maze, start, end):

    visited = {}
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    def recur(maze, cur, end):
        nonlocal visited, dx, dy
        if cur == end:
            return True
        r = len(maze)*cur[0] + cur[1]
        if visited.get(r, 0) == 1:
            return False
        
        visited[r] = True
        for k in range(4):

            x = cur[0]
            y = cur[1]

            while x>=0 and y>=0 and y<len(maze) and x<len(maze) and maze[x][y]==0:
                x += dx[k]
                y += dy[k]
            
            x -= dx[k]
            y -= dy[k]
            ret = recur(maze, [x, y], end)
            if ret:
                return ret
        return False

    return recur(maze, start, end)

test = '''
0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0
'''

maze = []
for r in test.split('\n'):
    if len(r.strip()) == 0:
        continue
    values = list(map(int, r.split(' ')))
    maze.append(values)

print(check_reachable(maze, [0,4], [3,2]))
print(check_reachable(maze, [0,4], [4,4]))
            