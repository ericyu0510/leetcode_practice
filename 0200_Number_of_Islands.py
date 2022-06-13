class Solution:
    # '''
    # Time: O(m*n)
    # Space: O(m*n)
    # '''
    # def numIslands(self, grid) -> int:
    #     self.grid = grid
    #     self.m, self.n = len(grid), len(grid[0])
    #     self.s = set()
    #     self.count = 0
    #     for i in range(self.m):
    #         for j in range(self.n):
    #             if (i, j) not in self.s:
    #                 if self.grid[i][j] == "1":
    #                     self.count += 1
    #                     self.DFS(i, j)
    #                 else:
    #                     self.s.add((i, j))
    #     return self.count
    # def DFS(self, row, col):
    #     if((row, col) not in self.s):
    #         self.s.add((row, col))
    #     if(self.grid[row][col] == "1"):
    #         if(row+1<self.m):
    #             self.DFS(row+1, col)
    #         if(col+1<self.n):
    #             self.DFS(row, col+1)
    #     return

    '''
    Time: O(m*n)
    Space: O(1)
    '''
    def numIslands(self, grid) -> int:
        def sink(i, j):
            if(0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1"):
                grid[i][j] = "0"
                list(map(sink, (i-1, i+1, i, i), (j, j, j-1, j+1)))
                return 1
            return 0
        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[0])))