# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.count = 0
        self.value = None
        self.inorder(root)
        return self.value
    
    def inorder(self, root):
        if self.count == self.k:
            return
        if root.left:
            self.inorder(root.left)
        if self.count == self.k:
            return
        self.count += 1
        self.value = root.val
        if root.right:
            self.inorder(root.right)
        return