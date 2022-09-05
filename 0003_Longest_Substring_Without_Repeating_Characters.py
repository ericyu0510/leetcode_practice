class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = defaultdict(int)
        l, r = -1, -1
        m_len = 0
        while(r < len(s)-1):
            r += 1
            if s[r] in d:
                l += 1
                while(s[l]!= s[r]):
                    del d[s[l]]
                    l += 1
            else:
                d[s[r]] += 1
                m_len = max(m_len, len(d))
        return m_len