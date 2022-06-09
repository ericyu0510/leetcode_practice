class Solution:
    '''
    Time: O(n)
    Space: O(1)
    
    '''
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r  = 0, len(numbers)-1
        while(l<r):
            if(numbers[l] + numbers[r] == target):
                return [l+1, r+1]
            if(numbers[l] + numbers[r-1] >= target):
                r -= 1
            else:
                l += 1