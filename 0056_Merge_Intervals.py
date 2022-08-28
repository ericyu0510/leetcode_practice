class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # if len(intervals)==1 :
        #     return intervals
        intervals.sort()
        ret = []
        start = 0
        end = 0
        
        while(end < len(intervals)):
            endi = intervals[start][1]
            while(end < len(intervals) and intervals[end][0] <= endi):
                endi = max(endi, intervals[end][1])
                end += 1
            ret.append([intervals[start][0], endi])
            start = end
        return ret