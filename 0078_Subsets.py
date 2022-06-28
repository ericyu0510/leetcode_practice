class Solution:
    '''
    Time: O(n* 2^n)
    Space: O(n* 2^n)
    '''
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     ans = []
    #     for i in range(2**len(nums)):
    #         l = []
    #         for j in range(len(nums)):
    #             if (i >> j) & 1:
    #                 l.append(nums[j])
    #         ans.append(l)
    #     return ans
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(1 << len(nums)):
            l = []
            for j in range(len(nums)):
                if (i >> j) & 1:
                    l.append(nums[j])
            ans.append(l)
        return ans