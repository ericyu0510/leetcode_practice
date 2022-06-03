# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    DFS
    '''
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if root is None:
#             return root
#         self.ret = []
#         self.countLevel(root, 0)
#         return self.ret
    
#     def countLevel(self, root, lev):
#         if(len(self.ret) < lev+1):
#             self.ret.append([root.val])
#         else:
#             self.ret[lev].append(root.val)
#         if(root.left):
#             self.countLevel(root.left, lev+1)
#         if(root.right):
#             self.countLevel(root.right, lev+1)
#         return
    '''
    BFS
    time: O(n)
    space: O(n)
    '''
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        if(root is None):
            return root
        
        q, ret = deque([root]), []
        while(q):
            cur_lev = []
            for _ in range(len(q)):
                node = q.popleft()
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
                cur_lev.append(node.val)
            ret.append(cur_lev)
        return ret