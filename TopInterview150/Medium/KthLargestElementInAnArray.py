import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, -num)

        p = 0

        while p < k-1:
            remove = heapq.heappop(heap)
            p += 1

        return -heapq.heappop(heap)