class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return False
        
        check_list = sorted(nums)

        for i in range(1, len(check_list)):
            if check_list[i] == check_list[i - 1]:
                return True

        return False