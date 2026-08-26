# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dicValues = {}

        while head:
            if head.val not in dicValues:
                dicValues[head.val] = 1
            else:
                dicValues[head.val] += 1
            head = head.next

        res = ListNode(0)
        current = res

        for key in dicValues:
            if dicValues[key] > 1:
                continue
            else:
                current.next = ListNode(key)
                current = current.next
                current.next = None

        return res.next