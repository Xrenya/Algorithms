class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        self.head = head
        self.max = -float("inf")
        def recusive_call(node):
            if node:
                if not recusive_call(node.next):
                    return False
                self.max = max(self.max, self.head.val + node.val)
                self.head = self.head.next
            return True

        recusive_call(head)
        return self.max
