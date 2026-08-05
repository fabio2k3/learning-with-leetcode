class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1 = 0
        p2 = len(height) - 1

        res = 0

        while p1 < p2:
            area = min(height[p1], height[p2]) * (p2 - p1)

            if area > res:
                res = area

            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1

        return res