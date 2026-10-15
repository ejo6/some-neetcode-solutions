class TreeNode:
    def __init__(self, val: str, isEnd: bool = False) -> None:
        self.val = val
        self.children = {}
        self.isEnd = isEnd


class PrefixTree:
    def __init__(self):
        self.rootNode = TreeNode('0')

    def insert(self, word: str) -> None:

        def dfInsert(char: str, root: TreeNode, isEnd=False) -> TreeNode:
            # Create the node only if this prefix doesn't exist yet
            if char not in root.children:
                root.children[char] = TreeNode(char)
            child = root.children[char]
            # Mark the end whether the node is new or already existed
            if isEnd:
                child.isEnd = True
            return child

        node = self.rootNode
        for c in word[:-1]:
            node = dfInsert(c, node)
        dfInsert(word[-1], node, isEnd=True)

    def search(self, word: str) -> bool:

        def dfSearch(index: int, node: TreeNode) -> bool:
            if index == len(word):
                return node.isEnd
            child = node.children.get(word[index])
            if child is None:
                return False
            return dfSearch(index + 1, child)

        return dfSearch(0, self.rootNode)

    def startsWith(self, prefix: str) -> bool:

        def dfSearch(index: int, node: TreeNode) -> bool:
            if index == len(prefix):
                return True
            child = node.children.get(prefix[index])
            if child is None:
                return False
            return dfSearch(index + 1, child)

        return dfSearch(0, self.rootNode)