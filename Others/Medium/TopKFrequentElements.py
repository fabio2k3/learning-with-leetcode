import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dic = {}

        for n in nums:
            dic[n] = dic.get(n, 0) + 1

        heap = []

        for key in dic:
            heapq.heappush(heap, (-dic[key], key))

        count = 0
        res = []

        while count < k:
            value , key = heapq.heappop(heap)
            res.append(key)
            count += 1

        return res