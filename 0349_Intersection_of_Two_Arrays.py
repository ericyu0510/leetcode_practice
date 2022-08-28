class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        Time: O(m+n) where m = len(nums1), n = len(nums2)
        Space: O(m+n)
        '''
        s1 = set(nums1)
        s2 = set(nums2)
        # if len(s2) > len(s1):
        #     s1, s2 = s2, s1
        # ret = []
        # for item in s1:
        #     if item in s2:
        #         ret.append(item)
        # return ret
        return list(s1&s2)