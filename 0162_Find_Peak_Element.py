class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while(l < r):
            mid = (l+r) // 2
            if mid == 0:
                if nums[mid+1] < nums[mid]:
                    return mid
                else:
                    l = mid +1
                    continue
            elif mid == len(nums)-1:
                if nums[mid-1] < nums[mid]:
                    return mid
                else:
                    r = mid -1
                    continue
            else:
                if nums[mid+1] > nums[mid]:
                    l = mid + 1
                    continue
                elif nums[mid-1] > nums[mid]:
                    r = mid - 1
                    continue
                else:
                    return mid
        # l == r return either of these
        return l