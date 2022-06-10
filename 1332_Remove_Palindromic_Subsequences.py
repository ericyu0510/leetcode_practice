class Solution:
    def removePalindromeSub(self, s: str) -> int:
        '''
        Time - O(n)
        Space - O(n)
        '''
        if(''.join(reversed(s)) == s):
            return 1
        else:
            return 2
        
        '''
        Time - O(n)
        Space - O(1)
        '''
        # return 2 - all(s[i] == s[~i] for i in range(len(s) // 2))