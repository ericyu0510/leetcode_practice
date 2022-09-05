# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     def goodNodes(self, root: TreeNode) -> int:
#         def dfs(root, m):
#             nonlocal good
#             if root == None:
#                 return
#             if root.val >= m:
#                 good += 1
#             dfs(root.left, max(m, root.val))
#             dfs(root.right, max(m, root.val))

#         good = 0
#         dfs(root, root.val)
#         return good

    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0
        self.dfs(root, root.val)
        return self.good
    def dfs(self, root, m):
        if root.val>= m:
            self.good+= 1
        m = max(m, root.val)
        if root.left:
            self.dfs(root.left, m)
        if root.right:
            self.dfs(root.right, m)