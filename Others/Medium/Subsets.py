class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []

        def complete_list(i, path):
            if i == len(nums):
                res.append(path[:])
                return
            complete_list(i + 1, path)
            path.append(nums[i])
            complete_list(i+1, path)
            path.pop()

        complete_list(0,[])
        return res