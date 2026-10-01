# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def inorder_list(raiz):
            result = []

            def inorder(nodo):
                if nodo is None:
                    return
                inorder(nodo.left)
                result.append(nodo.val)
                inorder(nodo.right)

            inorder(raiz)
            return result

        inorderList = inorder_list(root)

        if len(inorderList) == 1:
            return True

        for i in range(1, len(inorderList)):
            if inorderList[i] <= inorderList[i-1]:
                return False

        return True