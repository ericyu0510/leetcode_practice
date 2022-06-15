# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         p_route = self.find_element(root, p)
#         q_route = self.find_element(root, q)
#         i = 0
#         while(i < min(len(p_route), len(q_route))):
#             if p_route[i] != q_route[i]:
#                 break
#             i += 1
#         return p_route[i-1]
        
#     def find_element(self, root, target):
#         if root == target:
#             return [target.val]
#         else:
#             if(root.left):
#                 ret = self.find_element(root.left, target)
#                 if ret != None:
#                     return [root.val] + ret 
#             if(root.right):
#                 ret = self.find_element(root.right, target)
#                 if ret != None:
#                     return [root.val] + ret
#             return None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left != None and right != None: return root
        if left != None: return left
        return right
    