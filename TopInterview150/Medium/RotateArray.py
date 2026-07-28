class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        arrREs = [0]*n

        for i in range(n):
            arrREs[(i + k) % n] = nums[i]

        for j in range(n):
            nums[j] = arrREs[j]