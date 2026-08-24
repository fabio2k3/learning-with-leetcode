# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        elements = []

        while head:
            elements.append(head)
            head = head.next

        l = left - 1
        r = right - 1

        while l < r:
            nodePivot = elements[l]
            elements[l] = elements[r]
            elements[r] = nodePivot
            l += 1
            r -= 1

        res = ListNode(0)
        current = res

        for element in elements:
            current.next = element
            current = current.next
            current.next = None

        return res.next
