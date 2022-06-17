class Solution:
    '''
    Time: O(n log k)  since O(log k) for each push or pop
    Space: O(k)
    '''
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for x, y in points:
            neg_dist = -(x**2+y**2)
            heappush(max_heap, [neg_dist, x, y])
            if(len(max_heap)>k):
                heappop(max_heap)
        
        return [[x, y] for _, x, y in max_heap]
    
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         max_heap = []
#         for x, y in points:
#             neg_dist = -(x**2+y**2)
#             if(len(max_heap)== k):
#                 heappushpop(max_heap, [neg_dist, x, y])
#             else:
#                 heappush(max_heap, [neg_dist, x, y])
#         return [[x, y] for _, x, y in max_heap]