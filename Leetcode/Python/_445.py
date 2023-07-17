# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def recusive_reverse(self, head):
        if not head or not head.next:
            return head
        
        p = self.recusive_reverse(head.next)
        head.next.next = head
        head.next = None
        return p
    
    def reverse(self, head):
        prev = None
        temp = None
        while head:
            temp = head.next
            
            head.next = prev
            
            prev = head
            head = temp
            
        return prev
            
            
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.recusive_reverse(l1)
        l2 = self.recusive_reverse(l2)
        head = None
        carry = 0
        while l1 or l2:
            acc = 0
            if l1:
                acc += l1.val
                l1 = l1.next
            if l2:
                acc += l2.val
                l2 = l2.next
            
            carry += acc
            head = ListNode(carry % 10, head)
            carry //= 10
            
        if carry:
            head = ListNode(carry % 10, head)    
        
        return head
