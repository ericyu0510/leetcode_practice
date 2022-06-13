class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        m, n = len(grid), len(grid[0])
        q = deque()
        num_fresh = 0
        for i in range(m):
            for j in range(n):
                if(grid[i][j] == 2):
                    q.append((i, j))
                elif(grid[i][j] == 1):
                    num_fresh += 1 
        if(len(q) == 0):
            return -1 if num_fresh else 0
        time = -1
        while(q):
            time += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                if(i > 0 and grid[i-1][j] == 1):
                    num_fresh -= 1
                    grid[i-1][j] = 2
                    q.append((i-1, j))
                if(i < m-1 and grid[i+1][j] == 1):
                    num_fresh -= 1
                    grid[i+1][j] = 2
                    q.append((i+1, j))
                if(j > 0 and grid[i][j-1] == 1):
                    num_fresh -= 1
                    grid[i][j-1] = 2
                    q.append((i, j-1))
                if(j < n-1 and grid[i][j+1] == 1):
                    num_fresh -= 1
                    grid[i][j+1] = 2
                    q.append((i, j+1))
        
        return time if num_fresh == 0 else -1