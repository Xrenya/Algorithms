# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
# It is not compulsory to preserve the original relative order of the nodes in each of the two partitions.
# The task should be done in-place without creating additional ListNode

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = slow = fast = ListNode(0, head)

        count = 1
        while fast and fast.next:
            fast = fast.next
            count += 1

        prev = slow
        slow = slow.next
        ops = 0
        while count > ops:
            if slow.val < x:
                prev = slow
                slow = slow.next
            else:
                next_node = slow.next
                
                fast.next = slow
                fast = fast.next
                slow.next = None

                prev.next = next_node
                slow = next_node
            ops += 1

        return dummy.next
