class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # return len(s.split()[-1])
        
        end = len(s)-1
        count = 0
        while(s[end] == ' '):
            end -= 1
        while(end >= 0 and s[end] != ' '):
            count += 1
            end -= 1
        return count 