import heapq
import math
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap_distance = []

        for point in points:
            x = point[0]
            y = point[1]

            distance = math.sqrt(math.pow(x, 2) + math.pow(y,2))
            heapq.heappush(heap_distance, (distance, point))


        res = []

        while k > 0:
            dis, res_point = heapq.heappop(heap_distance)
            k -= 1

            res.append(res_point)
        return res