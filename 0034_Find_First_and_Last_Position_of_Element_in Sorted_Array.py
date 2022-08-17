from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0: return [-1, -1]
        ret = [-1, -1]
        start, end = 0, len(nums)-1
        while(start < end):
            mid = (start + end) // 2
            if nums[mid] == target:
                if mid == len(nums)-1 or nums[mid+1] != target:
                    ret[1] = mid
                    break
                else:
                    start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        if start == end and nums[start] == target: ret[1] = start

                
        start, end = 0, len(nums)-1
        while(start < end):
            mid = (start + end) // 2
            if nums[mid] == target:
                if mid == 0 or nums[mid-1] != target:
                    ret[0] = mid
                    break
                else:
                    end = mid - 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        if start == end and nums[start] == target: ret[0] = start

        return ret
a = Solution()
a.searchRange([2,2],2)
