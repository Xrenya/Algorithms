# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderListV2(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        self.head = head
        def dfs(node):
            if node:
                if not dfs(node.next):
                    return False
                if self.head == node or self.head.next == node:
                    node.next = None
                    return False
                next_node = self.head.next
                self.head.next = node
                node.next = next_node
                self.head = self.head.next.next

            return True

        dfs(head)
        return head
      
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        cur = slow.next
        slow.next = None

        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        cur = prev
        while head and cur:
            next_node = head.next
            head.next = cur
            cur_next = cur.next
            cur.next = next_node
            cur = cur_next
            head = next_node
