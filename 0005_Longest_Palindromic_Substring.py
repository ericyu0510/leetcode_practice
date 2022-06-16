class Solution:
    '''
    Button-up DP
    Time: O(n^2)
    Space: O(n^2)
    '''
#     def longestPalindrome(self, s: str) -> str:
#         longestP_start, longestP_len = 0, 1
#         n = len(s)
#         dp = [[False]*n for _ in range(n)]
#         for i in range(n):
#             dp[i][i] = True
        
#         for end in range(n):
#             for start in range(end-1, -1, -1):
#                 if s[start] == s[end]:
#                     if end-start == 1 or dp[start+1][end-1]:
#                         dp[start][end] = True
#                         P_len = end-start+1
#                         if P_len > longestP_len:
#                             longestP_len = P_len
#                             longestP_start = start
#         return s[longestP_start : longestP_start+longestP_len]
    
    '''
    Two pointers
    Time: O(n^2)
    Space: O(1)
    '''
    def longestPalindrome(self, s: str) -> str:
        longestP_start, longestP_len = 0, 1
        n = len(s)
        for i in range(n):
            right = i
            while(right < n and s[right]==s[i]):
                right += 1
            left = i-1
            while(right<n and left>=0 and s[right]==s[left]):
                right += 1
                left -= 1
            P_len = right-left-1
            if P_len > longestP_len:
                longestP_len = P_len
                longestP_start = left+1
        return s[longestP_start : longestP_start+longestP_len]
            