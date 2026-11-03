import heapq

class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        heap = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heapq.heappush(heap, matrix[i][j])

        count = 0
        res = 0

        while count < k:
            res = heapq.heappop(heap)

        return res