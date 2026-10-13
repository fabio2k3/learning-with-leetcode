import heapq
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        heap = []

        for lista in lists:
            while lista:
                heapq.heappush(heap, lista.val)
                lista = lista.next

        res = ListNode(0)
        current = res

        while heap:
            value = heapq.heappop(heap)
            current.next = ListNode(value)
            current = current.next

        return res.next