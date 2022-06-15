class Solution:
    '''
    Time: < O(n * n!)
    Space: O(n!)
    '''
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = [[nums[0]]]
        for i in range(1, len(nums)):
            for _ in range(len(ans)):
                perm = ans.pop(0)
                for j in range(i+1):
                    ans.append(perm[:j] + [nums[i]] + perm[j:])
        return ans