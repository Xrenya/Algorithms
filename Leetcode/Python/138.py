"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self,):
        self.map = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        if head in self.map:
            return self.map[head]
        
        node = Node(head.val)
        self.map[head] = node
        if head.next:
            node.next = self.copyRandomList(head.next)
        if head.random:
            node.random = self.copyRandomList(head.random)
        return node
