class Node:
    def __init__(self, key, val):
        # each node should have the key value pair
        self.key = key
        self.val = val
        self.prev, self.next = None, None

class LRUCache:
    """
    Key insight:

    get() can only be O(1) if we can instantly find the node of that element -> hashmap
    put() can only be O(1) if we can remove that element in O(1) -> hashmap,
          AND update the ordering of the elements in O(1) -> doubly linkedlist
    """

    def __init__(self, capacity: int):
        # key: node pairing
        self.capacity = capacity
        self.cache = {}
        # dummy nodes to track beginning and end
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def add(self, node):
        # insert this as the last node (but remember we have a dummy node)
        prev, last = self.right.prev, self.right
        node.prev, node.next = prev, last
        prev.next = node
        last.prev = node

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev


    def get(self, key: int) -> int:
        # check if key is valid
        if key in self.cache:
            # update this to appear at the end of the list (newest)
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        # check if key exists
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)

        # always insert regardless existence
        self.cache[key] = Node(key,value)
        self.add(self.cache[key])

        # check if capacity has reached
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
