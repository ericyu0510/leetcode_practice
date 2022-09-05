"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        '''
        Time: O(n)
        Space: O(width) width = width of widest level of the tree
        '''
        if not root:
            return []
        res = []
        q = [root]
        while(q):
            lev = []
            for _ in range(len(q)):
                cur = q.pop(0)
                lev.append(cur.val)
                if cur.children:
                    for child in cur.children:
                        q.append(child)
            res.append(lev)
        return res