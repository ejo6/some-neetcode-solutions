"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:

    def postorder(self, root: 'Node') -> List[int]:
        return self.traverse(root, []) if root else []
    
    def traverse(self, r, res) -> List[int]:
        if root is None: 
            return

        for c in r.children:
            self.traverse(c, res)
        res.append(r.val)
        return res
