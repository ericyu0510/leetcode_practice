class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        '''
        Time Complexity: O(n)
        Space Complexity: O(k), where k is the number of distinct elements. Here, k = 10⁴ (See constraints)
        '''
        # length = len(nums)
        # l = r = 0
        # hash_t = defaultdict(int)
        # max_score = 0
        # s = 0
        # while(r < length):
        #     hash_t[nums[r]] += 1
        #     s += nums[r]
        #     while(hash_t[nums[r]] == 2):
        #         hash_t[nums[l]] -= 1
        #         s -= nums[l]
        #         l += 1
        #     r += 1
        #     max_score = max(max_score, s)
        # return max_score
    
        
        l = r = 0
        s = set()
        max_score = 0
        score = 0
        while(r < len(nums)):
            if nums[r] not in s:
                s.add(nums[r])
                score += nums[r]
                max_score = max(max_score, score)
                r += 1 
            else:
                s.remove(nums[l])
                score -= nums[l]
                l += 1
        return max_score