class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dicFrec = {}

        for num in nums:
            if num not in dicFrec:
                dicFrec[num] = 1
            else:
                dicFrec[num] += 1

        res = 0
        n = len(nums)

        for key in dicFrec:
            if dicFrec[key] >= (n//2):
                res = key
                break

        return res