class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        m, n = len(matrix), len(matrix[0])
        max_path_memo = {}
        
        def traverse(mat, x, y, prev=None):
            nonlocal m, n
            if x >= m or y >= n or x < 0 or y < 0:
                return 0
            else:
                if prev is not None and prev > mat[x][y]:
                    return 0
                k = "{}_{}".format(x, y)
                if k in max_path_memo:
                    return max_path_memo[k]
                 
                bak = mat[x][y]
                mat[x][y] = -1
                max_path = 1 + max(
                    traverse(mat, x+1, y, bak),
                    traverse(mat, x-1, y, bak),
                    traverse(mat, x, y+1, bak),
                    traverse(mat, x, y-1, bak)
                )
                mat[x][y] = bak
                max_path_memo[k] = max_path
                return max_path
        
        for i in range(m):
            for j in range(n):
                path_len = traverse(matrix, i, j)
                max_path = max(max_path, path_len)
        return max_path
