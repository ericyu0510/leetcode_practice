from collections import Counter
# class Solution:
    # def minWindow(self, s: str, t: str) -> str:
    #     min_substr = ""
    #     min_len = float('inf')
    #     l, r = 0, 0
    #     count = Counter(t)
    #     m = len(s)
    #     st = set(t)
    #     while(r < m):
    #         while(any(c > 0 for c in count.values()) and r < m):
    #             if s[r] in st:
    #                 count[s[r]] -= 1
    #             r += 1
    #         while(all(c <= 0 for c in count.values()) and l < r):
    #             if s[l] in st:
    #                 count[s[l]] += 1
    #             l += 1
    #         if r == m:
    #             break
    #         if r - l +1 < min_len:
    #             min_substr = s[l-1:r]
    #             min_len = r - l +1
        
    #     if l>0 and s[l-1] in s:
    #         count[s[l-1]] -= 1
    #         if all(c <= 0 for c in count.values()) and r - l +1 < min_len:
    #             min_substr = s[l-1:r]

    #     return min_substr
    
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = Counter(t)
        min_str = ""
        min_str_len = len(s)+1
        l = 0
        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] -= 1
            while(all(c<=0 for c in count.values()) and l<=r):
                if r-l+1 < min_str_len:
                    min_str_len = r-l+1
                    min_str = s[l:r+1]
                if s[l] in count:
                    count[s[l]] += 1
                l += 1
        return min_str