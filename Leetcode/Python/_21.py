# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            listnode = None
            while l1 and l2:
                if l1.val > l2.val:
                    if listnode is None:
                        listnode = ListNode(l2.val)
                        cursor = listnode
                    else:
                        cursor.next = ListNode(l2.val)
                        cursor = cursor.next
                    l2 = l2.next
                else:
                    if listnode is None:
                        listnode = ListNode(l1.val)
                        cursor = listnode
                    else:
                        cursor.next = ListNode(l1.val)
                        cursor = cursor.next
                    l1 = l1.next
            while l1:
                cursor.next = ListNode(l1.val)
                l1 = l1.next
                cursor = cursor.next
            while l2:
                cursor.next = ListNode(l2.val)
                l2 = l2.next
                cursor = cursor.next
        return listnode
                
                
                
