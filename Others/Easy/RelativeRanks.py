import heapq
class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        heap_max = []

        for i in range(len(score)):
            heapq.heappush(heap_max, (-1*score[i], i))

        count = 1
        
        res = [""] * len(score)

        while heap_max:
            scr, place = heapq.heappop(heap_max)

            if count == 1:
                res[place] = "Gold Medal"
                count += 1
            elif count == 2:
                res[place] = "Silver Medal"
                count += 1
            elif count == 3:
                res[place] = "Bronze Medal"
                count += 1
            else:
                res[place] = str(count)
                count += 1

        return res
