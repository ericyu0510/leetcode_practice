class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         min_size = 10000000
#         cur_sum = 0
#         l = 0
#         for r in range(len(nums)):
#             cur_sum += nums[r]
#             while(cur_sum >= target):
#                 min_size = min(min_size, r-l+1)
#                 cur_sum -= nums[l]
#                 l += 1
            
#         return min_size if min_size < 10000000  else 0
        s = target
        min_size = len(nums)+1
        l = 0
        for r in range(len(nums)):
            s -= nums[r]
            while(s<=0):
                min_size = min(min_size, r-l+1)
                s += nums[l]
                l += 1
        return min_size%(len(nums)+1)
            