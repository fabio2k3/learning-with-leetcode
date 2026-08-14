# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        res = ListNode(0)
        current = res

        while list1 and list2:
            if list1.val < list2.val:
                current.next = ListNode(list1.val)
                current = current.next
                current.next = None
                list1 = list1.next
            else:
                current.next = ListNode(list2.val)
                current = current.next
                current.next = None
                list2 = list2.next

        while list1:
            current.next = ListNode(list1.val)
            current = current.next
            current.next = None
            list1 = list1.next

        while list2: 
            current.next = ListNode(list2.val)
            current = current.next
            current.next = None
            list2 = list2.next


        return res.next