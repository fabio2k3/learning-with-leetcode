class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        if n== 0:
            return 0
        if n == 1:
            return 1

        p = 1
        res = 1

        dicVal = {}
        pMove = p

        while p < n:
            if nums[p] != nums[p - 1] and nums[p] not in dicVal:
                dicVal[nums[p]] = 1
                res += 1
                p += 1
                val = nums[p]
                nums[pMove] = val
                pMove += 1
                
            else:
                while p < n and nums[p] == nums[p - 1]:
                    p += 1

        return res

        