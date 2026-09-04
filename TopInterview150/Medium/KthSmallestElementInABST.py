import heapq
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def full_list(raiz: Optional[TreeNode]):
            if raiz is None:
                return []
            return [raiz.val] + full_list(raiz.left) + full_list(raiz.right)

        listValues = full_list(root)
        heap = []

        for val in listValues:
            heapq.heappush(heap, val)

        res = -1
        count = 1
        while count <= k:
            res = heapq.heappop(heap)
            count += 1

        return res