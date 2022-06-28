class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        end = False
        i = 0
        ans = ""
        while(not end):
            if i < len(strs[0]):
                c = strs[0][i]
            else:
                end = True
                break
            for st in strs:
                if i > len(st)-1 or st[i] != c:
                    end = True
                    break
            if not end:
                ans = ans + c
                i += 1
        return ans