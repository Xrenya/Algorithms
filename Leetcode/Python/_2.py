# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode()
        runner = output
        reminder = 0
        while l1 or l2:
            cur_sum = reminder
            
            if l1:
                cur_sum += l1.val
                l1 = l1.next
            
            if l2:
                cur_sum += l2.val
                l2 = l2.next
            
            runner.next = ListNode(cur_sum % 10)
            runner = runner.next
            reminder = cur_sum // 10
        
        if reminder > 0:
            runner.next = ListNode(reminder)
        
        return output.next
        
       
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        val  = 0
        dummy = ListNode()
        listNode = dummy
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            val = val1 + val2 + carry
            carry = val // 10
            val %= 10
            listNode.next = ListNode(val)
            
            listNode = listNode.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next
