class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        node = ListNode(0, head)
        prev_node = node
        
        
        while head and head.next:
            first = head
            second = head.next
            
            prev_node.next = second
            first.next = second.next
            second.next = first
            
            prev_node = first
            head = first.next

        
        return node.next
    
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        first = second = head
        first = first.next
        flag = False
        while second.next:
            temp = second.val
            second.val = first.val
            first.val = temp
            second = first.next
            if not first.next or not second.next:
                break
            first = second.next
        return head
        
