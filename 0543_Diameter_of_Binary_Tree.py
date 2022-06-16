# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def DFS(root):
            # each DFS call return a list with 3 values, representing left_child_diameter(increasing), left_child_diameter(increasing),
            # and non_increasing_diameter
            ret_left, ret_right, l_n, r_n = 0, 0, 0, 0
            if(root.left):
                l_l, l_r, l_n = DFS(root.left)
                ret_left = max(l_l, l_r)+1
            if(root.right):
                r_l, r_r, r_n = DFS(root.right)
                ret_right = max(r_l, r_r)+1
                
            ret_non_increase = max(l_n, r_n, ret_left+ret_right)
            return [ret_left, ret_right, ret_non_increase]
        
        return max(DFS(root))

#     def diameterOfBinaryTree(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         self.ans = 0
        
#         def height(p):
#             # it's custom to define the height of an empty tree to be -1. This also fixes the off-by-one error I mentioned.
#             if not p: return -1       
                            
#             left, right = height(p.left), height(p.right)
            
#             # the "2+" accounts for the edge on the left plus the edge on the right. This change is required to account for 
#             # the fact that we updated the height of an empty tree to be -1. 
#             self.ans = max(self.ans, 2+left+right)   
            
#             return 1+max(left, right)
            
#         height(root)
#         return self.ans