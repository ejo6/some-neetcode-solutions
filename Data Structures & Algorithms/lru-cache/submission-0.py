class ListNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.front = None   # least recently used
        self.back = None    # most recently used

    def _remove(self, node: ListNode):
        if node.prev:
            node.prev.next = node.next
        else:
            self.front = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.back = node.prev
        node.prev = node.next = None

    def _append(self, node: ListNode):
        node.prev = self.back
        node.next = None
        if self.back:
            self.back.next = node
        else:
            self.front = node
        self.back = node

    def moveToBack(self, node: ListNode):
        if node is self.back:
            return
        self._remove(node)
        self._append(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.moveToBack(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.moveToBack(node)
            return

        if len(self.cache) >= self.capacity:
            lru = self.front
            self._remove(lru)
            del self.cache[lru.key]

        newNode = ListNode(key, value)
        self._append(newNode)
        self.cache[key] = newNode