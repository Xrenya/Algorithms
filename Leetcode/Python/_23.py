# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeList(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1

        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next

        head.next = self.mergeList(l1, l2)
        return head



    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        step = 1
        n = len(lists)
        while step < n:
            for i in range(0, n - step, step * 2):
                lists[i] = self.mergeList(lists[i], lists[i + step])
            step *= 2
        
        return lists[0] if n else None


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
