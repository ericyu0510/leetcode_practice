class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         return self.canSumToTarget(nums, sum(nums))
        
#     def canSumToTarget(self, nums: List[int], target: int) -> bool:
#         if target % 2 == 1 :
#             return False
#         elif target//2 in nums:
#             return True
#         canP = False
#         for i, num in enumerate(nums):
#             canP = canP or self.canSumToTarget(nums[:i]+nums[i+1:], target-2*num)
#             if canP:
#                 break
            
#         return canP
    
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum & 1:
            return False
        half_sum = sum(nums)//2
        dp = [True] + [False] * half_sum
        for num in nums:
            for i in range(half_sum, num-1, -1):
                dp[i] |= dp[i-num]
        return dp[half_sum]