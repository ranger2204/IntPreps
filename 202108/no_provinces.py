class Solution:
    def findCircleNum(self, isConnected: list) -> int:
        visited = {}
        def dfs(node_index, isConnected):
            if node_index in visited:
                return
            else:
                visited[node_index] = True
                for n in isConnected[node_index]:
                    dfs(n, isConnected)

        provinces = 0
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i, isConnected)
                provinces += 1
        return provinces