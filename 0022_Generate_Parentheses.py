class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def helper(s:str, l_bracket:int, r_bracket:int):
            s = s + '('
            if(l_bracket < n-1):
                tmp = s
                for i in range(min(n-r_bracket, l_bracket-r_bracket+1)):
                    tmp = tmp + ')'
                    helper(tmp, l_bracket+1, r_bracket+i+1)
                helper(s, l_bracket+1, r_bracket)
                return
            else:
                while(r_bracket < n):
                    s = s + ')'
                    r_bracket += 1
                ans.append(s)
            return
        helper('', 0, 0)
        return ans