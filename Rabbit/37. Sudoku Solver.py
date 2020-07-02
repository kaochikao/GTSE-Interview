"""
algo:
- 先找到要fill的cell -> empty stack
- 對每個座標都用1-9去試一次，看是否safe

- 這題歸類是DFS, 合理，因為一開始就先下一個值，然後跑到最後，看最後結果是否可以

Source:
https://github.com/qiyuangong/leetcode/blob/master/python/037_Sudoku_Solver.py
"""


class Solution(object):

    def solveSudoku(self, board):
        # empty is a stack, 這其實是先做一個座標系統，把empty coordinates記錄下來，以9進位制來表達一個座標，所以這個stack是todo list
        empty = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty.append(i * 9 + j)

        self.solve(board, empty)
        return board

    
    def solve(self, board, empty):

        if not empty:
            return True
        
        pos = empty[-1]
        row = pos // 9
        col = pos % 9

        for k in range(1, 10):
            
            if self.is_safe(board, row, col, str(k)):
                empty.pop()
                board[row][col] = str(k)
                tmp = self.solve(board, empty)

                if tmp:
                    return True
                else:
                    # 這裡就是坐到後面發現solve return False, 要rollback
                    empty.append(pos)
                    board[row][col] = '.'

        return False



    def is_safe(self, board, row, col, c):

        for i in range(9):
            if board[i][col] == c:
                return False
        
        for i in range(9):
            if board[row][i] == c:
                return False
        
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3

        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == c:
                    return False


        return True