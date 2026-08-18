# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ret = ListNode(-1)
        carry = 0
        while l1 and l2:
            carry += l1.val + l2.val
            ret.next = ListNode(carry % 10)
            carry //= 10
            ret = ret.next
            l1 = l1.next
            l2 = l2.next

        l1 = l1 if l1 else l2
        while l1:
            carry += l1.val
            ret.next = ListNode(carry % 10)
            carry //= 10
            ret = ret.next
            l1 = l1.next
        if carry:
            ret.next = ListNode(carry % 10)

        return dummy.next
