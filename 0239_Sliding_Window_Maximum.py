class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = collections.deque()
        out = []
        for i in range(len(nums)):
            while(d and nums[d[-1]] <= nums[i]):
                d.pop()
            d.append(i)
            if d[0] <= i-k:
                d.popleft()
            if i >= k-1:
                out.append(nums[d[0]])
        return out