from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_substr = ""
        min_len = float('inf')
        l, r = 0, 0
        count = Counter(t)
        m = len(s)
        st = set(t)
        while(r < m):
            while(any(c > 0 for c in count.values()) and r < m):
                if s[r] in st:
                    count[s[r]] -= 1
                r += 1
            while(all(c <= 0 for c in count.values()) and l < r):
                if s[l] in st:
                    count[s[l]] += 1
                l += 1
            if r == m:
                break
            if r - l +1 < min_len:
                min_substr = s[l-1:r]
                min_len = r - l +1
        
        if l>0 and s[l-1] in s:
            count[s[l-1]] -= 1
            if all(c <= 0 for c in count.values()) and r - l +1 < min_len:
                min_substr = s[l-1:r]

        return min_substr