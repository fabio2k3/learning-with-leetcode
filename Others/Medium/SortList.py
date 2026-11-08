# Definition for singly-linked list.
import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        heap = []

        while head:
            heapq.heappush(heap, head.val)
            head = head.next

        res = ListNode(0)
        current = res

        while heap:
            value = heapq.heappop(heap)
            current.next = ListNode(value)
            current = current.next

        return res.next