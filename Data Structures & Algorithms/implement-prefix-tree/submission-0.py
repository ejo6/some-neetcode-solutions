class TreeNode:
    def __init__(self, val: str, children: List[...] = None, isEnd: bool = False) -> None:
        self.val = val
        self.children = children if children else []
        self.isEnd = isEnd

class PrefixTree:
    def __init__(self):
        self.rootNode = TreeNode('0')

    def insert(self, word: str) -> None:
        # Iterate from root, appending
        
        def dfInsert(char: str, root: TreeNode, isEnd=False) -> TreeNode:
            # Prefix already exists so far: return that node
            for child in root.children:
                if char == child.val: 
                    if isEnd: child.isEnd = True 
                    return child
            # Create new node, append it, return that new node
            else:
                newNode = TreeNode(char, isEnd=isEnd)
                root.children.append(newNode)
                return newNode

        node = self.rootNode

        # Insert each node
        for c in word[:-1]:
            node = dfInsert(c, node)
        # Insert end node
        dfInsert(word[-1], node, isEnd=True)


    def search(self, word: str) -> bool:        

        def dfSearch(index: int, root: TreeNode) -> bool:
            # Base case: We found/are at the end
            if index == len(word):
                return root.isEnd

            for child in root.children:
                if child.val == word[index]: 
                    return dfSearch(index + 1, child)
            return False
        
        return dfSearch(0, self.rootNode)
            

    def startsWith(self, prefix: str) -> bool:
        def dfSearch(index: int, node: TreeNode) -> bool:
            if index == len(prefix):
                return True
            for child in node.children:
                if child.val == prefix[index]:
                    return dfSearch(index + 1, child)
            return False

        return dfSearch(0, self.rootNode)
            
        