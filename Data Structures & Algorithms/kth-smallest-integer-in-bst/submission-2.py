# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# if nodesVisited == (totalNodes - k + 1): return root.val


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        decreasingNodes = []

        def reverseInOrder(root: Optional[TreeNode]) -> int:
            if not root: return 
            
            reverseInOrder(root.right)
            decreasingNodes.append(root.val)
            reverseInOrder(root.left)

        reverseInOrder(root)
        return decreasingNodes[-k]

# [ ]

        