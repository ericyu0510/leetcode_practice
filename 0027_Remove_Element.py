class Solution:
    '''
    Time: O(n^2)
    Space: O(1)
    '''
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums)-1
        while(l <= r):
            while(l <= r and nums[l] != val):
                l += 1
            while(l <= r and nums[r] == val):
                r -= 1
            if l < r:
                nums[l]  = nums[r]
                l += 1
                r -= 1
        return l