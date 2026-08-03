class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 1:
            return 0

        if nums[0] == 0:
            return -1

        saltos = 0
        maxJump = 0
        finalActual = 0

        for i in range(0, n-1):
            maxJump = max(maxJump, i + nums[i])

            if i == finalActual:
                saltos += 1
                finalActual = maxJump

                if finalActual >= n - 1:
                    break

        return saltos 