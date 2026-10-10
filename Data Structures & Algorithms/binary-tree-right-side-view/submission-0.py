# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        def bfs(root: Optional[TreeNode]) -> List[List[int]]:
            if not root: return []

            result = []

            q = deque()
            q.append(root)
            level = 0

            while q:
                result.append([])

                for i in range(len(q)):
                    node = q.popleft()
                    result[level].append(node.val)

                    if node.left is not None: q.append(node.left)
                    if node.right is not None: q.append(node.right)
                level += 1
            return result

        levels = bfs(root)
        result = []
        
        for level in levels:
            result.append(level[-1])

        return result


