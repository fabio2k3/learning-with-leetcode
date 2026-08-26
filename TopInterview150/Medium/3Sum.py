class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        dicRes = {}

        n = len(nums)

        for i in range(n - 2):
            l, r = i + 1, n - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total == 0:
                    mi_tupla = (nums[i] , nums[l], nums[r])
                    if mi_tupla not in dicRes:
                        dicRes[mi_tupla] = 1
                    else:
                        dicRes[mi_tupla] += 1
                    l += 1
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1

        res = []

        for key in dicRes:
            element1, element2, element3 = key[0], key[1], key[2]
            lis_res = []
            lis_res.append(element1)
            lis_res.append(element2)
            lis_res.append(element3)
            res.append(lis_res)

        return res                