class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n = len(nums)

        l = 0
        r = n - 1

        if target < nums[0]:
            return 0
        if target > nums[n-1]:
            return n

        while l < r:
            m = (l + r) // 2

            if target == nums[m]:
                return m
            if target < nums[m]:
                r = m
            if target > nums[m]:
                l = m + 1

        return l