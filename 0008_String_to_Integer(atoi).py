class Solution:
    def myAtoi(self, s: str) -> int:
        if s == "":
            return 0
        i = 0
        ans = 0
        pos = True
        while(i < len(s) and s[i] == ' '):
            i += 1
        if(i < len(s)):
            if(s[i] == '+'):
                i += 1
            elif(s[i] == '-'):
                i += 1
                pos = False
        while(i < len(s) and s[i].isdecimal()):
            ans = ans*10 + int(s[i])
            i += 1
        if ans > 2147483647:
            return 2147483647 if pos else -2147483648
        return ans if pos else -ans