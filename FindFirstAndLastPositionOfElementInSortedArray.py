class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        res = [-1, -1]
        
        l = 0
        r = len(nums) - 1

        # First
        while l < r:
            m = (l + r) // 2

            if nums[m] == target:
                res[0] = m
                r = m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m

        # Last
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] == target:
                res[1] = m
                l = m + 1
            elif nums[m] < target:
                l = m + 1
            else:
                r = m

        return res
