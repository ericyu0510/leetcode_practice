class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums: return
        pivot = random.choice(nums)
        larger = [num for num in nums if num > pivot]
        mid = [num for num in nums if num == pivot]
        smaller = [num for num in nums if num < pivot]
        if len(larger) >= k:
            return self.findKthLargest(larger, k)
        elif len(larger) + len(mid) < k:
            return self.findKthLargest(smaller, k-len(larger)-len(mid))
        else:
            return mid[0]