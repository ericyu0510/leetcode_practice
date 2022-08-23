class Solution:
    # def isPowerOfFour(self, n: int) -> bool:
    #     if n <= 0:
    #         return False
    #     while(n > 1):
    #         if n % 4 != 0:
    #             return False
    #         n = n // 4
    #     return True
    
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n&(n-1) == 0 and n & 0b1010101010101010101010101010101 == n