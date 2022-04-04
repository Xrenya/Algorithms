# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        array = []
        while temp:
            array.append(temp.val)
            temp = temp.next
        
        array[k - 1], array[len(array) - k] = array[len(array) - k], array[k - 1]
        
        head = ListNode(0)
        dummy = head
        for num in array:
            dummy.next = ListNode(num)
            dummy = dummy.next
            
        return head.next
            
        
