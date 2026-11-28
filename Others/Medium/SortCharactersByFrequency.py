import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}

        for c in s:
            if c not in dic:
                dic[c] = 1
            else:
                dic[c] += 1

        heap_max = []

        for key in dic:
            heapq.heappush(heap_max, (-1 * dic[key], key))

        res = ""
        while heap_max:
            freq , val = heapq.heappop(heap_max)
            freq *= (-1)

            for _ in range(freq):
                res += val 

        return res