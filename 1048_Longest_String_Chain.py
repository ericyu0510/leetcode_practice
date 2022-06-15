class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        for s in sorted(words, key=len):
            dp[s] = max(dp.get(s[:i]+s[i+1:], 0) + 1 for i in range(len(s)))
        return max(dp.values())