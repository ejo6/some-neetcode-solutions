# BFS by LEVEL down the tree
# when we dont have children of a tree, indicate that.


class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = ""

        def preorderSerialize(root: Optional[TreeNode]) -> str:
            nonlocal result

            if not root: 
                result += "-,"
                return

            result += f"{root.val},"

            preorderSerialize(root.left)
            preorderSerialize(root.right)

            return result

        preorderSerialize(root)        
        print(result)
        return result # 1,2,-,-,3,4,-,-,5,-,-,
    
        
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
                    

            

