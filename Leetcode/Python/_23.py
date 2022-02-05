# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# https://stackoverflow.com/questions/40205223/priority-queue-with-tuples-and-dicts
from queue import PriorityQueue


class Get:
    def __init__(self, first, second):
        self.first, self.second = first, second
    
    def __lt__(self, other):
        return self.first < other.first


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put(Get(l.val, l))
        head = point = ListNode(0)
        while not q.empty():
            use_object = q.get()
            val = use_object.first
            node = use_object.second
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put(Get(node.val, node))
        return head.next
