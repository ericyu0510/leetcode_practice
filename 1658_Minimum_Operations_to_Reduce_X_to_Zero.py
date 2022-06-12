class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
#         '''
#         Prefix Sum + Suffix sum = x
#         '''
#         length = len(nums)
#         ps_left = [nums[0]]*length
#         ps_right = [nums[-1]]*length
#         for i in range(1, len(nums)):
#             ps_left[i] = ps_left[i-1] + nums[i]
#             ps_right[-i-1] = ps_right[-i] + nums[-i-1]
        
#         min_op = float('inf')
#         l, r = 0, 1
#         while(l < length and ps_left[l] <= x):
#             if(ps_left[l] == x):
#                 min_op = min(min_op, l+1)
#                 l += 1
#                 continue
#             else:
#                 while(r < length and ps_right[r] >= x - ps_left[l] and l + length-r < length):
#                     if(ps_right[r] == x - ps_left[l]):
#                         min_op = min(min_op, (l+1)+(length-r))
#                         break
#                     else:
#                         r += 1
#                 l += 1
                        
#         l, r = length-2, length-1
#         while(r > -1 and ps_right[r] <= x):
#             if(ps_right[r] == x):
#                 min_op = min(min_op, length-r)
#                 r -= 1
#                 continue
#             else:
#                 while(l > -1 and ps_left[l] >= x - ps_right[r] and l + length-r < length):
#                     if(ps_left[l] == x - ps_right[r]):
#                         min_op = min(min_op, (l+1)+(length-r))
#                         break
#                     else:
#                         l -= 1
#                 r -= 1
#         return -1 if min_op == float('inf') else min_op
        '''
        Longest subarray whose sum is sum(numbers) - x
        '''
        target = sum(nums) - x
        curr_sum, max_len = 0, 0
        start_idx = 0
        found = False
        for end_idx in range(len(nums)):
            curr_sum += nums[end_idx]
            while start_idx <= end_idx and curr_sum > target:
                curr_sum -= nums[start_idx]
                start_idx += 1
            if curr_sum == target:
                found = True
                max_len = max(max_len, end_idx - start_idx + 1)

        return len(nums) - max_len if found else -1
    