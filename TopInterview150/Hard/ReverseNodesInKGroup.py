# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        list_Nodes = []

        while head:
            list_Nodes.append(head)
            head = head.next

        if k >= 2 and len(list_Nodes) >= 2:
            p1 = 0
            p2 = k - 1

            while p1 < len(list_Nodes) and p2 < len(list_Nodes):
                l = p1
                r = p2
                while l < r:
                    pivotNode = list_Nodes[l]
                    list_Nodes[l] = list_Nodes[r]
                    list_Nodes[r] = pivotNode

                    l += 1
                    r -= 1

                p1 += k
                p2 += k

        res = ListNode(0)
        current = res

        for i in range(len(list_Nodes)):
            current.next = list_Nodes[i]
            current = current.next
            current.next = None

        return res.next