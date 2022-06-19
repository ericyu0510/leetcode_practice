from collections import deque
class Solution:
    '''
    DP
    Time: O(mn)
    Space: O(mn)
    '''
    def uniquePaths(self, m: int, n: int) -> int:
        q = deque()
        q.append((0,0))
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        while(q):
            count = 0
            for _ in range(len(q)):
                r, c = q.popleft()
                if r > 0:
                    dp[r][c] += dp[r-1][c]
                if c > 0:
                    dp[r][c] += dp[r][c-1]
                if count == 0 and c < n-1:
                    q.append((r, c+1))
                if r < m-1:
                    q.append((r+1, c))
                count += 1
        return dp[m-1][n-1]