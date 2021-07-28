# https://leetcode.com/problems/sudoku-solver/

class Solution:

    def check_in_box(self, i, j, board):
        box_x = i // 3
        box_y = j // 3
        marked = [False for x in range(0, 9)]
        for x in range(box_x*3, (box_x+1)*3):
            for y in range(box_y*3, (box_y+1)*3):
                if board[x][y] != '.':
                    marked[int(board[x][y])-1] = True

        return [x+1 for x, v in enumerate(marked) if v is False]

    def check_along_row(self, i, j, board):
        marked = [False for x in range(0, 9)]
        for x in range(0, len(board)):
            if board[x][j] != '.':
                marked[int(board[x][j])-1] = True
        
        return [x+1 for x, v in enumerate(marked) if v is False]

    def check_along_column(self, i, j, board):
        marked = [False for x in range(0, 9)]
        for y in range(0, len(board[0])):
            if board[i][y] != '.':
                marked[int(board[i][y])-1] = True
        
        return [x+1 for x, v in enumerate(marked) if v is False]

    def get_valid_entry(self, i, j, board):
        valid_along_row = self.check_along_row(i, j, board)
        valid_along_col = self.check_along_column(i, j, board)
        valid_in_box = self.check_in_box(i, j, board)

        return list(map(str, list(set(valid_along_col) & set(valid_along_row) & set(valid_in_box))))

    def get_next_empty_cell(self, board):
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == '.':
                    return (x,y)
        return (-1, -1)
            
    def solveSudoku(self, board: list):
        """
        Do not return anything, modify board in-place instead.
        """
        
        def recur(i, j, board):

            if i == j == -1:
                return True

            valids = self.get_valid_entry(i, j, board)
            
            if len(valids) == 0:
                return False

            for v in valids:
                board[i][j] = v
                x, y = self.get_next_empty_cell(board)
                if recur(x, y, board) is True:
                    return True
                board[i][j] = '.'
            
            board[i][j] = '.'
            return False
        

        x, y = self.get_next_empty_cell(board)
        recur(x, y, board)
        return board
            
            
        
tests = [
    {
        'board': [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]
    }
]

for t in tests:
    result = Solution().solveSudoku(**t)
    for r in result:
        print(r)
