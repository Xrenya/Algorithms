# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return ListNode().next
        
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
            
        k = k % len(nums)
        head = ListNode()
        dummy = head
        for i in range(len(nums)):
            dummy.next = ListNode(nums[-k+i])
            dummy = dummy.next
        return head.next
