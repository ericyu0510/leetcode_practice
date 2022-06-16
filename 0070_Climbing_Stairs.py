class Solution:
    def climbStairs(self, n: int) -> int:
        '''Recursion TC:O(2^n)'''
        # if(n == 1):
        #     return 1
        # elif(n ==2):
        #     return 2
        # else:
        #     return self.climbStairs(n-1) + self.climbStairs(n-2)
        
        '''
        Math
        '''
        # from math import factorial
        # ways = 0
        # max2 = n//2
        # for n_step2 in range(max2+1):
        #     ways += int(factorial(n-n_step2)/(factorial(n-2*n_step2)*factorial(n_step2)))
        # return ways
        
        
        '''
        DP
        Time:O(n)
        Space:O(n)
        '''
        dp = [-1]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[-1]