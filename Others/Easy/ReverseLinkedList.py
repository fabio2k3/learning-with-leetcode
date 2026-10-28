# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        nums = []

        while head:
            nums.append(head.val)
            head = head.next

        nums.reverse()
        res = ListNode(0)
        current = res

        for n in nums:
            current.next = ListNode(n)
            current = current.next

        return res.next