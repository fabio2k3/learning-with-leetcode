# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        strNum1 = ""
        strNum2 = ""

        if l1 is None:
            return l2
        if l2 is None: 
            return l1 

        while l1:
            strNum1 += str(l1.val)
            l1 = l1.next

        while l2:
            strNum2 += str(l2.val)
            l2 = l2.next

        sumNumbers = int(strNum1[::-1]) + int(strNum2[::-1])

        strResult = str(sumNumbers)
        strResult = strResult[::-1]

        res = ListNode(0)
        current = res

        p = 0
        n = len(strResult)

        while p < n:
            value = int(strResult[p])
            current.next = ListNode(value)
            current = current.next
            current.next = None
            p += 1

        return res.next