# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def preorden(myTree, result=None):
            if result is None:
                result = []
            if myTree:
                result.append(myTree.val)
                preorden(myTree.left, result)
                preorden(myTree.right, result)
            return result

        values = preorden(root)
        values.sort()

        ans = float("inf")
        for i in range(1, len(values)):
            ans = min(ans, values[i] - values[i - 1])

        return ans