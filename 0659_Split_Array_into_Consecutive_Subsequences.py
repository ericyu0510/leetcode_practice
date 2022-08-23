class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        d = defaultdict(int)
        end = collections.Counter()
        for num in nums:
            d[num] += 1
            
        for num in nums:
            if d[num] == 0:
                continue
            elif end[num-1]:
                d[num] -= 1
                end[num-1] -= 1
                end[num] += 1
            elif d[num+1] and d[num+2]:
                d[num] -= 1
                d[num+1] -= 1
                d[num+2] -= 1
                end[num+2] += 1
            else:
                return False
        return True
            
            