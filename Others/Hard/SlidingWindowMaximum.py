import heapq
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        heap = []
        res = []

        for i, x in enumerate(nums):
            heapq.heappush(heap, (-x, i))

            if i >= k - 1:                       
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                res.append(-heap[0][0])          

        return res