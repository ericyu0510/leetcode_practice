class Solution:
    def countAndSay(self, n: int) -> str:
        def count(s:str):
            new_s = ""
            count = 1
            for i in range(1,len(s)):
                if s[i] == s[i-1]:
                    count += 1
                else:
                    new_s  = new_s + str(count) + s[i-1]
                    count = 1
            new_s  = new_s + str(count) + s[-1]
            return new_s
                    
#         def cas(s: str, cur:int, n: int) -> str:
#             new_s = count(s)
#             if cur == n:
#                 return new_s
#             else:
#                 return cas(new_s, cur+1, n)
            
#         if n == 1: return "1"
#         else:
#             return cas("1", 2, n)
        cur = 1
        s = "1"
        while(cur < n):
            s = count(s)
            cur += 1
        return s