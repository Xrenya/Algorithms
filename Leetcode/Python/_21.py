# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list2 is None:
            return list1
        elif list1 is None:
            return list2

        if list1.val > list2.val:
            head = list2
            list2 = list2.next
        else:
            head = list1
            list1 = list1.next

        head.next = self.mergeTwoLists(list1, list2)

        return head
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        result = head 
        
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1 is None and list2 is None:
            return []
        
        while list1 and list2:
            if list1.val > list2.val:
                head.next = ListNode(list2.val)
                list2 = list2.next
                head = head.next 
            else:
                head.next = ListNode(list1.val)
                list1 = list1.next
                head = head.next 
                
        while list2:
            head.next = ListNode(list2.val)
            list2 = list2.next
            head = head.next 
        while list1:
            head.next = ListNode(list1.val)
            list1 = list1.next
            head = head.next 
            
        return result.next
    
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            listnode = ListNode()
            cursor = listnode
            while l1 and l2:
                if l1.val > l2.val:
                    cursor.next = ListNode(l2.val)
                    cursor = cursor.next
                    l2 = l2.next
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
        return listnode.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        temp = head
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        if list1:
            temp.next = list1
        if list2:
            temp.next = list2
        return head.next
