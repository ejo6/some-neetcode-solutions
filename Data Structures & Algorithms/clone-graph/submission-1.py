"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# Start 1 the first node
# 1. append list of all neighbours
# 2. mark the node as seen
# 3. go the the lowest, unexplored node

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        
        clones = {}

        def dfs(node: Optional['Node']) -> 'Node':
            if node in clones:
                return clones[node]

            copy = Node(node.val)
            clones[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)
        


