class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for st in strs:
            tup = tuple(sorted(st))
            d[tup].append(st)
        return list(d.values())
            