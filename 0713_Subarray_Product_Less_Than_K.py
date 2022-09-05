class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        p = 1
        l = 0
        ret = 0
        for r in range(len(nums)):
            p *= nums[r]
            while(p >= k and l < r):
                p /= nums[l]
                l += 1
            if p < k:
                ret += r-l+1
        return ret
                