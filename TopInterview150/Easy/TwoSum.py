class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicValues = {}

        res = []

        for i in range(0, len(nums)):
            numCheck = target - nums[i]
            if numCheck in dicValues:
                res.append(dicValues[numCheck])
                res.append(i)
                break
            else:
                dicValues[nums[i]] = i


        return res