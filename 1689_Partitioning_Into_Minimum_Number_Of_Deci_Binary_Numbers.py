class Solution:
    def minPartitions(self, n: str) -> int:
        # max_ord = 0
        # for c in n:
        #     max_ord = max(max_ord, ord(c))
        # return int(chr(max_ord))
        return int(max(n))