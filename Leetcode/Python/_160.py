# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def counter(head):
            h = head
            count = 0
            while h:
                h = h.next
                count += 1
            return count
        
        a_counter = counter(headA)
        b_counter = counter(headB)
        diff = abs(b_counter - a_counter)
        
        while diff != 0:
            if b_counter < a_counter:
                headA = headA.next
            else:
                headB = headB.next
            diff -= 1
            
        while headB != headA:
            headA = headA.next
            headB = headB.next
        return headB

            
                
    
