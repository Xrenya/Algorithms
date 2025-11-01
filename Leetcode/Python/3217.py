# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        dummy = ListNode(0, head)
        cur = dummy
        while cur and cur.next:
            if cur.next.val in nums:
                while cur and cur.next and cur.next.val in nums:
                    cur.next = cur.next.next
                if cur:
                    cur = cur.next
            else:
                cur = cur.next

        return dummy.next
