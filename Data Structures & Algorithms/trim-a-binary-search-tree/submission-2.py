# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]: 
        
        def trim(root: Optional[TreeNode]):
            if not root: 
                return 

            while root.left and root.left.val < low:
                root.left = root.left.right

            while root.right and root.right.val > high:
                root.right = root.right.left
            
            trim(root.left)
            trim(root.right)

        while root and not (low <= root.val <= high):
            if root.val < low: 
                root = root.right
            else:
                root = root.left
        
        trim(root)
        return root if root else None






        # Recurse through each node (preorder)
        # if the node is low, it becomes its right node
        # if the node is high, it becomes its left node
        # *Once a node changes, need to check if it is in bounds, if not, try next node

        # Set a dummy root with child actual root
        # Run algorithm:
        #   if the left child is too low, leftchild = leftchild.rightchild, try again if it is still too low
        #   if the right child is too high, rightchild = rightchild.leftchild, try again if it is still too low




