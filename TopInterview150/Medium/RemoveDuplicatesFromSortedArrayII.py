class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        dicVal = {}

        for i in range(2):
            if nums[i] not in dicVal:
                dicVal[nums[i]] = 1
            else:
                dicVal[nums[i]] += 1

        p = 2
        res = 2
        
        pMove = p
        
        while p < n:
            if (nums[p] != nums[p - 1] and nums[p] not in dicVal) or (nums[p] == nums[p - 1] and dicVal[nums[p]] == 1):
                res += 1
                val = nums[p]
                nums[pMove] = val
                pMove += 1

                if nums[i] not in dicVal:
                    dicVal[nums[p]] = 1
                else:
                    dicVal[nums[p]] += 1

                p += 1
                
            else:
                while p < n and nums[p] == nums[p - 1]:
                    p += 1
        
        return res