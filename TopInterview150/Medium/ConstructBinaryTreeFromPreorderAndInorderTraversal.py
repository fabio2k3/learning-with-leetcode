# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        inorder_index = {val: i for i, val in enumerate(inorder)}

        preIdx = 0

        def helper_func(left, right):
            nonlocal preIdx

            if left > right:
                return None

            rootVal = preorder[preIdx]
            preIdx += 1

            root = TreeNode(rootVal)

            mid = inorder_index[rootVal]

            root.left = helper_func(left, mid - 1)
            root.right = helper_func(mid + 1, right)

            return root

        return helper_func(0, len(inorder) - 1)