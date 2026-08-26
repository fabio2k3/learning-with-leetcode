# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lisNumber = []

        while head:
            lisNumber.append(head.val)
            head = head.next

        orgList = [0]*len(lisNumber)

        p = 0

        for i in range(len(lisNumber)):
            if lisNumber[i] < x:
                orgList[p] = lisNumber[i]
                p += 1

        for j in range(len(lisNumber)):
            if lisNumber[j] >= x:
                orgList[p] = lisNumber[j]
                p += 1

        res = ListNode(0)
        current = res

        for value in orgList:
            current.next = ListNode(value)
            current = current.next
            current.next = None


        return res.next