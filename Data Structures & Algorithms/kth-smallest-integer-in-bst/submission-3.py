# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# if nodesVisited == (totalNodes - k + 1): return root.val


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        increasingNodes = []

        def inOrder(root: Optional[TreeNode]) -> None:
            if not root: return 
            if len(increasingNodes) == k: return
            
            inOrder(root.left)
            increasingNodes.append(root.val)
            inOrder(root.right)

        inOrder(root)
        print(increasingNodes)
        return increasingNodes[k - 1]

        