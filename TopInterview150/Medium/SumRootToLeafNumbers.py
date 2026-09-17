# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        def calculateSum(mytree, sumActual):
            if mytree is None:
                return 0

            sumActual = sumActual * 10 + mytree.val
            
            if mytree.left is None and mytree.right is None:
                return sumActual

            return calculateSum(mytree.left, sumActual) + calculateSum(mytree.right, sumActual)

        return calculateSum(root, 0)

            