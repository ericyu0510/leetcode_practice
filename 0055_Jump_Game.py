class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        Time: O(n)
        Space: O(1)
        '''
        front = 0
        for i in range(len(nums)):
            if i > front:
                return False
            front = max(front, i + nums[i])
        return True