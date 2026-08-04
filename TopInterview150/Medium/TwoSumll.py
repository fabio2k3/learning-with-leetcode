class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []

        dic_values_pos = {}

        n = len(numbers)

        for i in range(n):
            num = numbers[i]
            check = target - num

            if check in dic_values_pos:
                res.append(dic_values_pos[check] + 1)
                res.append(i + 1)

                break
            else:
                dic_values_pos[num] = i


        return res