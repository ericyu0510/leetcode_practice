class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = 0
        d = dict()
        d[0] = 1
        count = 0
        for i in range(len(nums)):
            pre_sum += nums[i]
            count += d.get(pre_sum-k, 0)
            d[pre_sum] = d.get(pre_sum, 0) + 1
            
        return count