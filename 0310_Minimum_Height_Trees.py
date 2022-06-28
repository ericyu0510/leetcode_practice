from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        def DFS_helper(start, n):
            self.dist, self.parent = [-1]*n, [-1]*n
            self.dist[start] = 0
            DFS(start)
            return self.dist.index(max(self.dist))
        
        def DFS(index):
            for neib in graph[index]:
                if self.dist[neib] == -1:
                    self.dist[neib] = self.dist[index] + 1
                    self.parent[neib] = index
                    DFS(neib)
        
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        
        ind = DFS_helper(0, n)
        ind2 = DFS_helper(ind, n)
        
        cur = ind2
        path = []
        while(cur != -1):
            path.append(cur)
            cur = self.parent[cur]
        
        Q = len(path)
        return list(set([path[Q//2], path[(Q-1)//2]]))