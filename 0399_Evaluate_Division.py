from collections import defaultdict
from typing import *
class Solution:
    def solveQuery(self, u, v):
        if u not in self.graph:
            return -1.0
        if u == v:
            return 1.0
        
        self.visited.add(u)
        for elem, val in self.graph[u]:
            if elem == v:
                return val
        for elem, val in self.graph[u]:
            if elem not in self.visited:
                rec = self.solveQuery(elem, v)
                if rec != -1.0:
                    return val*rec
        return -1.0
    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.graph = defaultdict(set)
        for [u, v], val in zip(equations, values):
            self.graph[u].add((v, val))
            self.graph[v].add((u, 1/val))
        
        res = []
        for [u, v] in queries:
            self.visited = set()
            res.append(self.solveQuery(u, v))
        return res

a = Solution()
print(a.calcEquation([["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]],
[3.0,4.0,5.0,6.0],
[["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]))