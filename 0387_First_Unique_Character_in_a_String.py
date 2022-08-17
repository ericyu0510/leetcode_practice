from collections import OrderedDict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = OrderedDict()
        dup_s = set()
        for i in range(len(s)):
            if s[i] in dup_s:
                continue
            if s[i] in d:
                del d[s[i]]
                dup_s.add(s[i])
            else:
                d[s[i]] = i
        return d.popitem(last=False)[1] if d else -1

a = Solution()
a.firstUniqChar("leetcode")