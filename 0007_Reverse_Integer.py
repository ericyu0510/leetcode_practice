class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            neg = True
            x = -x
        rev = 0
        while(x > 0):
            rev = 10*rev + (x%10)
            x = x // 10
        if rev > 2**31-1 or rev < -2**31:
            return 0
        return -rev if neg else rev
        
        