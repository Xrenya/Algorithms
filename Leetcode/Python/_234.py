# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        
        middle = self.middleNode(head)
        reverse = self.reverseList(middle)
        
        
        while reverse:
            if reverse.val != head.val:
                return False
            head = head.next
            reverse = reverse.next
        return True
        
        
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow= slow.next
        return slow
    
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            next_curr = curr.next
            curr.next = prev
            prev = curr        
            curr = next_curr
        return prev
