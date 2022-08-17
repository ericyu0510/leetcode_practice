class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2): #need at least 3 numbers
            j, k = i+1, len(nums)-1
            while(j<k):
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return s
                if abs(target-s) < abs(target-closest):
                    closest = s
                if target-s > 0:
                    j += 1
                else:
                    k -= 1
        return closest
                    