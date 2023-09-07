class Solution:
    def reverse(self, node, right):
        if right == 1:
            return node
        new_head = self.reverse(node.next, right - 1)
        next_head = node.next
        node.next = next_head.next
        next_head.next = node
        return new_head

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == 1:
            self.reverse(head, right)

        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head
