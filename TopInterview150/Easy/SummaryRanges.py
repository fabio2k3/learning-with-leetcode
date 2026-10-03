class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        n = len(nums)

        if n == 0:
            return []

        if n == 1:
            return [str(nums[-1])]

        l = 0
        r = l + 1
        res = []

        while r < n:
            if nums[r] - nums[r-1] == 1:
                r += 1
            else:
                if r - l == 1:
                    res.append(str(nums[l]))
                else:
                    val1 = str(nums[l])
                    val2 = str(nums[r-1])
                    res.append(val1 + "->" + val2)

                l = r
                r = l + 1
  
        if r - l == 1:
            res.append(str(nums[l]))
        else:
            res.append(str(nums[l]) + "->" + str(nums[r-1]))

        return res