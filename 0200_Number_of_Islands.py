from typing import *
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

    # '''
    # Time: O(m*n)
    # Space: O(1)
    # '''
    # def numIslands(self, grid) -> int:
    #     def sink(i, j):
    #         if(0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1"):
    #             grid[i][j] = "0"
    #             list(map(sink, (i-1, i+1, i, i), (j, j, j-1, j+1)))
    #             return 1
    #         return 0
    #     return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[0])))
    
    def numIslands(self, grid: List[List[str]]) -> int:

        count = 0
        m, n = len(grid), len(grid[0])
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    self.dfs(grid, r, c)
                    count += 1
        return count
    
    def dfs(self,grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = "-1"
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
    

    # Or another

    # def numIslands(self, grid: List[List[str]]) -> int:
    #     def dfs(row, col):
    #         q = [(row, col)] #queue
    #         grid[row][col] = "-1"
    #         while(q):
    #             r, c = q.pop(0)
    #             if r>0 and grid[r-1][c]=="1":
    #                 q.append((r-1, c))
    #                 grid[r-1][c]="-1"
    #             if r<m-1 and grid[r+1][c]=="1":
    #                 q.append((r+1, c))
    #                 grid[r+1][c]="-1"
    #             if c>0 and grid[r][c-1]=="1":
    #                 q.append((r, c-1))
    #                 grid[r][c-1]="-1"
    #             if c<n-1 and grid[r][c+1]=="1":
    #                 q.append((r, c+1))
    #                 grid[r][c+1]="-1"
    #         return
            
    #     count = 0
    #     m, n = len(grid), len(grid[0])
    #     for r in range(m):
    #         for c in range(n):
    #             if grid[r][c] == "1":
    #                 dfs(r, c)
    #                 count += 1
    #     return count

a = Solution()
a.numIslands([["1","1","1"],["0","1","0"],["1","1","1"]])