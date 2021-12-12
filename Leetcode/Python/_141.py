# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow  = fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                return True
        return False

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        turtle = head
        rabbit = head
        while turtle and rabbit and rabbit.next:
            turtle = turtle.next
            rabbit = rabbit.next.next
            
            if turtle == rabbit:
                return True
        return False
