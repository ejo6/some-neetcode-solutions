class TrieNode:
    __slots__ = ("children", "isEnd")

    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            i = ord(c) - 97  # ord('a') == 97
            if node.children[i] is None:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.isEnd = True

    def _walk(self, s: str):
        node = self.root
        for c in s:
            node = node.children[ord(c) - 97]
            if node is None:
                return None
        return node

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        return self._walk(prefix) is not None