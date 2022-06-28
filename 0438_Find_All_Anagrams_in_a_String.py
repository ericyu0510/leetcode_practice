from collections import deque, defaultdict
class Solution:
    '''
    Time: O(len(s)+len(p))
    Space: O(len(p)) len(p) for both deque and defaultdict and set
    '''
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        q = deque()
        d = defaultdict(int)
        for c in p:
            d[c] += 1
        st = set(p)
        for i in range(len(s)):
            q.append(s[i])
            if s[i] in st:
                d[s[i]] -= 1
            if len(q) > len(p):
                pl = q.popleft()
                if pl in st:
                    d[pl] += 1
            if not any(d.values()):
                ans.append(i-len(p)+1)
        return ans