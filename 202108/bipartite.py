class Solution:
    def isBipartite(self, graph: list) -> bool:
        n = len(graph)
        node_colors = {}
        visited = {}

        def mark(graph, cur_node=0, color=0):
            visited[cur_node] = True
            if cur_node in node_colors:
                if node_colors[cur_node] != color:
                    return False
                return True
            else:
                node_colors[cur_node] = color
                
                for n in graph[cur_node]:
                    r = mark(graph, n, (color+1)%2)
                    if r is False:
                        return False
                return True

        for i in range(n):
            if i not in visited:
                c = node_colors.get(i, 0)
                r = mark(graph, i, c)
                if r is False:
                    return False
        return True

tests = [
    [[1,2,3],[0,2],[0,1,3],[0,2]],
    [[1,3],[0,2],[1,3],[0,2]],
]

for t in tests:
    print(Solution().isBipartite(t))