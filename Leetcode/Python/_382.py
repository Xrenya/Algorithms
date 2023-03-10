# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.indexes = self.count()

    def count(self):
        lst = []
        head = self.head
        idx = 0
        while head:
            lst.append(idx)
            idx += 1
            head = head.next
        return lst

    def getRandom(self) -> int:
        index = random.choice(self.indexes)
        head = self.head
        for _ in range(index):
            head = head.next
        return head.val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
