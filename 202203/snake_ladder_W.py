class Solution:
    def find_min_turns(self, snakes, ladders, MAX_SIZE=100):
        grid = {}
        for i in range(1, 101):
            grid[i] = [i+j for j in range(1, 7) if i+j <=100]

        class vertex:
            def __init__(self, v, d):
                self.v = v
                self.d = d
        
        q = [vertex(1, 1)]
        visited = {}
        while len(q) > 0:
            q_len = len(q)
            while q_len > 0:
                n = q.pop(0)
                if n.v not in visited:
                    visited[n.v] = n
                    if n.v in snakes:
                        q.append(vertex(snakes[n.v], n.d))
                    
                    elif n.v in ladders:
                        q.append(vertex(ladders[n.v], n.d))
                    
                    else:
                        for i in range(1, 7):
                            if n.v + i <= 100:
                                q.append(vertex(n.v+i, n.d+i))
                q_len -= 1
            
        return visited[100].d

test = {
    'snakes': {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78},
    'ladders': {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
}

print(Solution().find_min_turns(test['snakes'], test['ladders']))