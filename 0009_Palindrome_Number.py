class Solution:
    def isPalindrome(self, x: int) -> bool:
        # return str(x)[::-1] == str(x)
        if x < 0:
            return False
        orig = x
        new = 0
        while(x>0):
            new = new*10 + x%10
            x = x//10
        return new == orig        