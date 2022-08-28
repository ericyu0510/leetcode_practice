from typing import *
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr) < 3: return 0
        climbing = False
        descend= False
        l, r = 0, 1
        longest = 0
        while(r < len(arr)):
            if arr[r] < arr[r-1]:
                if climbing:
                    descend = True
                    r += 1
                else:
                    l = r
                    r += 1
            elif arr[r] == arr[r-1]:
                if climbing and descend:
                    longest = max(longest, r-l)
                    l = r-1
                    climbing  = False
                    descend = False
                else:
                    climbing = False
                    descend = False
                    l = r
                    r += 1
            else:
                if climbing and descend:
                    longest = max(longest, r-l)
                    l = r-1
                    climbing  = False
                    descend = False
                else:
                    climbing = True
                    r += 1
        if climbing and descend:
            longest = max(longest, r-l)
        return longest

a = Solution()
a.longestMountain([0,0,1,0,0,1,1,1,1,1])