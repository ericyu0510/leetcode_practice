class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = defaultdict(int)
        first = dict()
        res = 0
        degree = 0
        for i, elem in enumerate(nums):
            first.setdefault(elem, i)
            count[elem] += 1
            if count[elem] > degree:
                degree = count[elem]
                res = i - first[elem] + 1
            elif count[elem] == degree:
                res = min(res, i - first[elem] + 1)
        return res