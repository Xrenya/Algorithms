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
        
