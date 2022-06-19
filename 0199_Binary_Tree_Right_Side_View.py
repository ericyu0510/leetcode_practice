# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.maxh = 0
        self.ans =[]
        self.DFS(1, root)
        return self.ans
 
    def DFS(self, h, rt):
        if rt == None:
            return
        if h > self.maxh:
            self.ans.append(rt.val)
            self.maxh = h
        self.DFS(h+1, rt.right)
        self.DFS(h+1, rt.left)
        return
       