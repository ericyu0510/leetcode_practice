from typing import *
from collections import defaultdict
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        count_oil = [(0, startFuel)]
        last = 0
        d = defaultdict(int)
        d[0] = startFuel
        for cur_pos, fuel in stations:
            if len(count_oil) == 0: return -1
            for _ in range(len(count_oil)):
                count, oil = count_oil.pop(0)
                if oil - (cur_pos - last) >= 0:
                    d[count] = oil-(cur_pos-last)
                    count_oil.append( (count, oil-(cur_pos-last)) )
                    if count+1 not in d or d[count+1] < oil-(cur_pos-last)+fuel:
                        d[count+1] = oil-(cur_pos-last)+fuel
                        count_oil.append( (count+1, oil-(cur_pos-last)+fuel) )
            last = cur_pos
        m = float('inf')
        for count, oil in count_oil:
            if oil - (target-last) >= 0 and count < m:
                m = count
        return m

a = Solution()
a.minRefuelStops(1000,1,[[1,186],[145,161],[183,43],[235,196],[255,169],[263,200],[353,161],[384,190],[474,44],[486,43],[567,48],[568,96],[592,36],[634,181],[645,167],[646,69],[690,52],[732,28],[800,42],[857,55],[922,63],[960,141],[973,13],[977,112],[997,162]])
