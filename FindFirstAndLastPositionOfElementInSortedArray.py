class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]

        res = [-1, -1]

        # First 
        l = 0
        r = n - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        if nums[l] == target:
            res[0] = l

        # Last 
        l = 0
        r = n - 1
        while l < r:
            m = (l + r + 1) // 2
            if nums[m] > target:
                r = m - 1
            else:
                l = m
        if nums[l] == target:
            res[1] = l

        return res