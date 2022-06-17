"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    '''
    Time: O(V+E)
    Space: O(V) because of the hash table
    '''
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        hash_t = dict()

        def DFS(node, ntc): # node and node to copy
            for neitc in ntc.neighbors: # neighbor to copy
                if neitc.val not in hash_t:
                    new_node = Node(neitc.val, None)
                    hash_t[neitc.val] = new_node
                    node.neighbors.append(hash_t[neitc.val])   
                    DFS(new_node, neitc)
                else:    
                    node.neighbors.append(hash_t[neitc.val])    

        new_node = Node(node.val, None)
        hash_t[node.val] = new_node
        DFS(new_node, node)
        return new_node