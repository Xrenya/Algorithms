class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = {}
        self.tail = ListNode(-1, -1)
        self.head = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1

        node = self.nodes[key]
        self.remove(node)
        self.add(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            remove_old_node = self.nodes[key]
            self.remove(remove_old_node)

        node = ListNode(key, value)
        self.nodes[key] = node
        self.add(node)

        if len(self.nodes) > self.capacity:
            node_delete = self.head.next
            self.remove(node_delete)
            del self.nodes[node_delete.key]

    def add(self, node):
        previous_node = self.tail.prev
        previous_node.next = node
        node.prev = previous_node
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
