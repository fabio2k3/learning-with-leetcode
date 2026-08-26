# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        elements = []

        while head:
            elements.append(head.val)
            head = head.next

        n = len(elements)

        rotateList = [0]*n

        for i in range(n):
            rotateList[(i + k) % n] = elements[i]

        res = ListNode(0)
        current = res

        for i in range(n):
            current.next = ListNode(rotateList[i])
            current = current.next
            current.next = None


        return res.next