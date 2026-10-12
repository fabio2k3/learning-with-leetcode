# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return None
        
        dic_val = {}

        while head:
            if head.val not in dic_val:
                dic_val[head.val] = 1
            
            head = head.next

        res = ListNode(0)
        current = res

        for key in dic_val:
            current.next = ListNode(key)
            current = current.next
            current.next = None

        return res.next
        