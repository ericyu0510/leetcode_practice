class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return [x[0] for x in Counter(nums).most_common(k)]
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        
        h = [] # heap
        from heapq import heappush, heappushpop
        
        for key in d:
            if len(h) < k:
                heappush(h, (d[key], key))
            else:
                heappushpop(h, (d[key], key))
        
        return [x[1] for x in h]
        