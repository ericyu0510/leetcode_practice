class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dup = False
        l, r = 1, 1
        while(r < len(nums)):
            if nums[r] == nums[r-1]:
                if not dup:
                    dup = True
                    nums[l] = nums[r]
                    l += 1
                    r += 1
                else:
                    r += 1
            else:
                dup = False
                nums[l] = nums[r]
                l += 1
                r += 1
        return l