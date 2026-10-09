# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def countGoodNodes(root: TreeNode, largestAncestor: int) -> int:
            if not root: return 0
            
            # Potentially update the largest ancestor of a node
            largestAncestor = max(root.val, largestAncestor)
            isGood = int(root.val >= largestAncestor)

            return (countGoodNodes(root.left, largestAncestor) + countGoodNodes(root.right, largestAncestor) + isGood)

        return countGoodNodes(root, root.val)





        # Key insight: we need to track what the GREATEST node before hand was. Use a DFS

