from typing import *
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(idx: int, path: List[int], cur: int):
            if cur == target:
                res.append(path)
            if cur > target:
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                dfs(i+1, path+[candidates[i]], cur+candidates[i])
        candidates.sort()
        dfs(0, [], 0)
        return res
a = Solution()
a.combinationSum2([10,1,2,7,6,1,5], 8)