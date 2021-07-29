class Solution:
    def validPath(self, n: int, edges: list, start: int, end: int) -> bool:
        g = [[0 for i in range(n)] for i in range(n)]
        for e in edges:
            s, t = e
            g[s][t] = 1
            g[t][s] = 1
        
        def traverse(g, cur, tgt):
            if cur == tgt:
                return True
            else:
                for i, v in enumerate(g[cur]):
                    if v == 1:
                        g[cur][i] = 0
                        r = traverse(g, i, tgt)
                        g[cur][i] = 1
                        if r is True:
                            return r
                return False
        
        
        return traverse(g, start, end)
        
        