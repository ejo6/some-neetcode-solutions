# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# q: 7 6 
# r: [[1], [2, 3], [4, 5, 6, 7]]

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        result = []
        q = deque()
        
        q.appendleft(root)
        level = 0

        while q:
            size = len(q)
            result.append([])

            for i in range(size):
                curr = q.pop()
                result[level].append(curr.val)

                if curr.left is not None:
                    q.appendleft(curr.left)

                if curr.right is not None:
                    q.appendleft(curr.right)
        
            level += 1

        return result