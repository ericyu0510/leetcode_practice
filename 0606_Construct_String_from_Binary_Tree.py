# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def tree2str(self, root: Optional[TreeNode]) -> str:
#         self.res = [str(root.val)]
#         self.dfs(root)
#         return ''.join(self.res)
        
#     def dfs(self, root: Optional[TreeNode]):
#         if root.left or root.right:
#             self.res.append('(')
#             if root.left:
#                 self.res.append(str(root.left.val))
#                 self.dfs(root.left)
#             self.res.append(')')
#             if root.right:
#                 self.res.append("("+ str(root.right.val))
#                 self.dfs(root.right)
#                 self.res.append(')')

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        res = str(root.val)
        if root.left:
            res += '(' + self.tree2str(root.left) + ')'
        if not root.left and root.right:
            res += '()'
        if root.right:
            res += '(' + self.tree2str(root.right) + ')'
        return res