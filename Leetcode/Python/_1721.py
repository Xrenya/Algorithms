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
            
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        slow = fast = cnt = head
        counter = 0
        while cnt:
            counter += 1
            cnt = cnt.next
            
        for _ in range(k - 1):
            slow = slow.next
            
        for _ in range(counter - k):
            fast = fast.next
        
        slow.val, fast.val = fast.val, slow.val
        return head
        
