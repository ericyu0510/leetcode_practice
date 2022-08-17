class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        p = defaultdict(set)
        for i in range(len(pattern)):
            p[pattern[i]].add(i)
        for word in words:
            w = defaultdict(set)
            for j in range(len(word)):
                w[word[j]].add(j)
            if list(p.values()) == list(w.values()):
                ans.append(word)
        return ans