class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        for num in nums:
            if num >= target:          
                return 1

        if sum(nums) < target:
            return 0
        
        l = 0
        r = l + 1

        sum_parcial = nums[0]
        res = len(nums) + 1

        while r < len(nums):
            if sum_parcial >= target:   
                if (r - l) < res:
                    res = r - l
                sum_parcial -= nums[l]
                l += 1
            else:
                sum_parcial += nums[r]
                r += 1

        while sum_parcial >= target:    
            if (len(nums) - l) < res:
                res = len(nums) - l
            sum_parcial -= nums[l]
            l += 1

        if res != len(nums) + 1:
            return res
        else:
            return 0