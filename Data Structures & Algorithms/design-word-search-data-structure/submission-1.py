class TrieNode:
    def __init__(self, val: str, isEnd = False) -> None:
        self.val = val
        self.children = [None] * 26
        self.isEnd = isEnd


class WordDictionary:
    def __init__(self):
        # Dummy root
        self.root = TrieNode('0')

    def addWord(self, word: str) -> None:
        node = self.root

        for c in word:
            i = ord(c) - ord('a')
            if not node.children[i]:
                node.children[i] = TrieNode(c)
            node = node.children[i]

        node.isEnd = True


    def search(self, word: str) -> bool:
        def dfs(node: TrieNode, i: int) -> bool:
            if i == len(word):
                return True if node.isEnd else False

            # Handle .
            if word[i] == '.':
                for child in node.children:
                    if child: 
                        if dfs(child, i + 1): return True
                return False

            # Normal letters:
            j = ord(word[i]) - ord('a')
            if node.children[j]:
                return dfs(node.children[j], i + 1)

            return False

        return dfs(self.root, 0)







