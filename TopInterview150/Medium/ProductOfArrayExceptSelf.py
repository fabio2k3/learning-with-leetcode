class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        if n == 1:
            return nums

        leftMult = [0]*n
        rightMult = [0]*n

        leftMult[0] = nums[0]
        rightMult[-1] = nums[-1]

        for i in range(1,n):
            leftMult[i] = leftMult[i-1] *  nums[i]

        for i in range(n-2, -1, -1):
            rightMult[i] = rightMult[i + 1] * nums[i]

        res = [0]*n

        res[0] = rightMult[1]
        res[-1] = leftMult[-2]

        for i in range(1, n-1):
            res[i] = leftMult[i-1] * rightMult[i+1]

        return res