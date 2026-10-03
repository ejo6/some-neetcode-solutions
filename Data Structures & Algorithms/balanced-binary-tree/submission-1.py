# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.balanced = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.depth(root)
        return self.balanced

    def depth(self, root):
        if not self.balanced: return 0
        if root == None: return 0

        leftHeight = self.depth(root.left)
        rightHeight = self.depth(root.right)

        print(f"comparing {leftHeight} with {rightHeight}")
        if leftHeight - rightHeight < -1 or leftHeight - rightHeight > 1: self.balanced = False

        return max(leftHeight, rightHeight) + 1