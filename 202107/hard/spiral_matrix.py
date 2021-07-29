from abc import ABCMeta


class Solution:
    def generateMatrix(self, n: int) -> list:

        mat = [[-1 for _ in range(n)] for _ in range(n)]

        def recur(mat, i, j, n, c, d='r'):
            if n == 0:
                return
            
            if d == 'r':
                if j >= n or mat[i][j] != -1:
                    recur(mat, i+1, j-1, n, c, d='d')
                else:
                    mat[i][j] = c
                    recur(mat, i, j+1, n, c+1, d)
            
            elif d == 'd':
                if i >= n or mat[i][j] != -1:
                    recur(mat, i-1, j-1, n, c, d='l')
                else:
                    mat[i][j] = c
                    recur(mat, i+1, j, n, c+1, d)
            
            elif d == 'l':
                if j < 0 or mat[i][j] != -1:
                    recur(mat, i-1, j+1, n, c, d='u')
                else:
                    mat[i][j] = c
                    recur(mat, i, j-1, n, c+1, d)
            
            elif d == 'u':
                if i < 0 or mat[i][j] != -1:
                    recur(mat, i+1, j+1, n-1, c, d='r')
                else:
                    mat[i][j] = c
                    recur(mat, i-1, j, n, c+1, d)

        recur(mat, 0, 0, n, 1)
        return mat

class Solution2:
    def generateMatrix(self, n: int) -> list:
        mat = [[-1 for _ in range(n)] for _ in range(n)]


        c = n
        v = 1
        sx = sy = 0
        while c > 0:
            x = sx
            y = sy

            while y < sy + c:
                mat[x][y] = v
                v += 1
                y += 1

            y -= 1
            x += 1

            while x < sx + c:
                mat[x][y] = v
                v += 1
                x += 1
            
            x -= 1
            y -= 1

            while y >= sy:
                mat[x][y] = v
                v += 1
                y -= 1

            y += 1
            x -= 1
            
            while x > sx:
                mat[x][y] = v
                v += 1
                x -= 1
            
            sy += 1
            sx += 1
            c -= 2

        return mat


            
            


tests = [i for i in range(1, 8)]
for t in tests:
    mat = Solution2().generateMatrix(t)
    for r in mat:
        print(r)
    print()
