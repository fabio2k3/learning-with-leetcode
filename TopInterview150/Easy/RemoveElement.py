class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p = len(nums)
        for i in range(len(nums)):
            if nums[i] == val and i < p:
                p = i
            elif nums[i] != val and i > p:
                nums[p] = nums[i]
                nums[i] = val

                while p < len(nums):
                    if nums[p] == val:
                        break
                    p += 1

        res = 0

        p2 = 0

        while p2 < len(nums):
            if nums[p2] != val:
                res += 1
            else:
                break

        return res