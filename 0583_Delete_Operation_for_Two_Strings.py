class Solution:
    '''
    Top-down DP
    '''
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def DP(i: int, j: int):
            if (i, j) not in memo:
                if i == len(word1) or j == len(word2):
                    ans = len(word1) - i + len(word2) - j
                elif word1[i] != word2[j]:
                    ans = min(DP(i+1, j) + 1, DP(i, j+1) + 1)
                else:
                    ans = DP(i+1, j+1)
                memo[(i, j)] = ans
            return memo[(i, j)]
        return DP(0, 0)