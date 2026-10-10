# BFS by LEVEL down the tree
# when we dont have children of a tree, indicate that.


class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []
        def preorder(root: Optional[TreeNode]) -> None:
            if not root: 
                result.append('-')
                return

            result.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ",".join(result)
    
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        stack = []
        for c in reversed(data.split(",")):
            if c == "": continue
            if c == "-":
                stack.append(None)
            else:
                node = TreeNode(int(c))
                node.left = stack.pop()
                node.right = stack.pop()
                stack.append(node)
        return stack[0]
                    

            

