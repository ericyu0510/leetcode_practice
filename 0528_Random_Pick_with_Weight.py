class Solution:

    def __init__(self, w: List[int]):
        '''
        Time: O(n)
        Space: O(n)
        '''
        self.w = w
        for i in range(1, len(w)):
            self.w[i] += self.w[i-1]
        
    def pickIndex(self) -> int:
        '''
        Time: O(log n)
        Space: O(n)
        '''
        target = random.randint(1, self.w[-1])
        
        l, r = 0, len(self.w)-1
        while(l < r):
            mid = l + (r-l)//2
            if self.w[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return l
                

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()