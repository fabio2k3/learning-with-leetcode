# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dic_Node = {}

        while head:
            if head not in dic_Node:
                dic_Node[head] = 1
            else:
                return True
            head = head.next

        return False