class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ret = []
        def dfs(num: int, last_dig: int, level: int):
            nonlocal ret
            num = 10*num + last_dig
            if level+1 == n:
                ret.append(num)
                return
            for nxt_dig in range(10):
                if nxt_dig - (num%10) in {k, -k}:
                    dfs(num, nxt_dig, level+1)
        
        for i in range(1, 10):
            dfs(0, i, 0)
        return ret