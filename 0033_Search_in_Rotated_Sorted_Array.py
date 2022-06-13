class Solution:
    def search(self, nums: List[int], target: int) -> int:
        self.nums = nums
        last = nums[-1]
        if(nums[-1]<nums[0]):
            gap = self.find_gap(0, len(nums)-2, last)
            if(target > last):
                return self.binary_search(0, gap, target)
            else:
                return self.binary_search(gap+1, len(nums)-1, target)
        else:
            return self.binary_search(0, len(nums)-1, target)
            
     
    def find_gap(self, l, r, last):
        mid = (l + r) // 2
        if(self.nums[mid]>self.nums[mid+1]):
            return mid
        elif(self.nums[mid] > last):
            return self.find_gap(mid+1, r, last)
        else:
            return self.find_gap(l, mid-1, last)
        
    def binary_search(self, l, r, target):
        while l <= r:
            mid = (l + r) // 2
            if self.nums[mid] < target:
                l = mid + 1
            elif self.nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return -1