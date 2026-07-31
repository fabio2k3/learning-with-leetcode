class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        if n == 1:
            return True
        if nums[0] == 0:
            return False

        maxJump = -1

        for i in range(0, n - 1):
            if nums[i] >= n - 1 - i:
                return True
            maxJump = max(maxJump - 1, nums[i])

            if maxJump <= 0:
                return False


        return False