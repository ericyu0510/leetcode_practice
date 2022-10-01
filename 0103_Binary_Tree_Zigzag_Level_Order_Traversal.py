# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return []
#         direction = 1
#         queue = deque([root])
#         res = []
        
#         while queue:
#             level = []
#             for i in range(len(queue)):
#                 node = queue.popleft()
#                 level.append(node.val)
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#             res.append(level[::direction])
#             direction *= (-1)
#         return res

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        deq = deque([root])
        l2r = True
        while(deq):
            lev = []
            for _ in range(len(deq)):
                if l2r:
                    node = deq.popleft()
                    lev.append(node.val)
                    if node.left:
                        deq.append(node.left)
                    if node.right:
                        deq.append(node.right)
                else:
                    node = deq.pop()
                    lev.append(node.val)
                    if node.right:
                        deq.appendleft(node.right)
                    if node.left:
                        deq.appendleft(node.left)
            res.append(lev)
            l2r = not l2r
        return res