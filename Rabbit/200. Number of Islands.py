"""
algo
- for loop中rec, 但因為有記得走過哪些，所以可以skip
-------------------------------------------
edge case:

不能只move right & move down, 有回鉤形島嶼:
111
010
111
"""


class Solution:
    def numIslands(self, grid) -> int:

        ans = 0

        if len(grid) == 0:
            return ans

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.rec(grid, i, j)
                    ans += 1

        return ans

    def rec(self, grid, i, j):

        curr = grid[i][j]
        if curr == '-':
            return
        elif curr == '0':
            grid[i][j] = '-'
            return
        else:
            grid[i][j] = '-'
            if j + 1 < len(grid[0]):
                self.rec(grid, i, j + 1)
                
            if j - 1 > -1:
                self.rec(grid, i, j - 1)

            if i + 1 < len(grid):
                self.rec(grid, i + 1, j)
                
            if i - 1 > -1:
                self.rec(grid, i - 1, j)