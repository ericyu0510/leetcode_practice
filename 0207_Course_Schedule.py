class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        self.adj_dict = defaultdict(set)
        self.Visited = [0] * numCourses
        self.loop = False
        for k, v in prerequisites:
            self.adj_dict[k].add(v)
        # We need to interate from every vertex since the dag can be not connected
        for i in range(numCourses):
            if self.loop: break
            self.DFS(i)
        
        return self.loop == 0
        
    def DFS(self, start):
        if(self.loop): # early stop if a loop was found
            return
        if(self.Visited[start] == 1): # find a loop
            self.loop = 1
            return
        elif(self.Visited[start] == 0):
            self.Visited[start] = 1
            for neib in self.adj_dict[start]:
                self.DFS(neib)
            self.Visited[start] = 2
            return