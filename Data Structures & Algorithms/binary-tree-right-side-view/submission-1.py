# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        result = []

        q = deque()
        q.append(root)

        while q:
            qSize = len(q)

            for i in range(qSize):
                node = q.popleft()
                if i == qSize - 1: result.append(node.val)

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        return result

        


