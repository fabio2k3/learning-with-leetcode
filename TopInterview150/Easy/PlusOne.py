class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        numStr = ""

        for n in digits:
            numStr += str(n)

        resStr = str(int(numStr) + 1)

        res_List = []

        for c in resStr:
            res_List.append(int(c))

        return res_List