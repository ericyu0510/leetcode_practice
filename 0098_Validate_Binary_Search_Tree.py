# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.valid = True
        self.DFS(-float('inf'), float('inf'), root)
        return self.valid
    
    def DFS(self, min, max, root: Optional[TreeNode]):
        if(not min < root.val < max):
            self.valid = False
            return
        if(root.left):
            self.DFS(min, root.val, root.left)
        if(root.right):
            self.DFS(root.val, max, root.right)
        