# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = ListNode(0, head)
        current = front
        prefix = 0
        prefix2node = {0: front}

        while current:
            prefix += current.val
            prefix2node[prefix] = current
            current = current.next

        prefix = 0
        current = front
        
        while current:
            prefix += current.val
            current.next = prefix2node[prefix].next
            current = current.next

        return front.next


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = ListNode(0, head)
        start = front

        while start:
            prefix = 0
            end = start.next

            while end:
                prefix += end.val
                if prefix == 0:
                    start.next = end.next
                
                end = end.next

            start = start.next

        return front.next
