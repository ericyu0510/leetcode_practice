class Solution:
    def intToRoman(self, num: int) -> str:
        s = {0:'', 1:'I', 2:"II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7:"VII", 8:"VIII", 9:"IX", 10: "X", 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
        dig = 1
        ans = ""
        while(num > 0):
            c = num%10
            if c in {4, 9}:
                ans = s[c*dig] + ans
            elif c in {1,2,3}:
                for _ in range(c):
                    ans = s[dig] + ans
            elif c in {5,6,7,8}:
                for _ in range(c%5):
                    ans = s[dig] + ans
                ans = s[5*dig] + ans
            dig *= 10
            num = num//10
        return ans

a = Solution()
a.intToRoman(670)