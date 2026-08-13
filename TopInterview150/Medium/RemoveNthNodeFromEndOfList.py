# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lis_Num = []

        while head:
            lis_Num.append(head.val)
            head = head.next

        for i in range(len(lis_Num)):
            if i == len(lis_Num) - n:
                lis_Num.pop(i)

        res = ListNode(0)
        current = res

        for num in lis_Num:
            current.next = ListNode(num)
            current = current.next
            current.next = None

        return res.next