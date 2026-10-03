# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.same = True
     
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.checkSame(p, q)
        return self.same
        
    def checkSame(self, p, q):
        if not self.same: return
        if p is None and q is None: 
            return
        elif p is not None and q is None: 
            self.same = False
            return
        elif p is None and q is not None: 
            self.same = False # case of p null and q exists
            return
        elif (p.val != q.val): 
            self.same = False
            return
        
        self.checkSame(p.left, q.left)  
        self.checkSame(p.right, q.right)