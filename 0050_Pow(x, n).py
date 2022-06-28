class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.00000
        if n < 0:
            n = -n
            x = 1/x
        pow_left = n
        ans = 1
        while(pow_left):
            p = 1
            tmp = x
            while(2*p <= pow_left):
                tmp *= tmp
                p *= 2
            ans *= tmp
            pow_left -= p
        return round(ans, 5)