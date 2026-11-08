class Solution:
    def intToRoman(self, num: int) -> str:
        list_roman = [
            [1000, "M"],
            [900, "CM"],
            [500, "D"],
            [400, "CD"],
            [100, "C"],
            [90, "XC"],
            [50, "L"],
            [40, "XL"],
            [10, "X"],
            [9, "IX"],
            [5, "V"],
            [4, "IV"],
            [1, "I"]
        ]

        p = 0
        res = ""
        n = num

        while n > 0 and p < len(list_roman):
            if n >= list_roman[p][0] and p < len(list_roman):
                while n >= list_roman[p][0]:
                    res += list_roman[p][1]
                    n -= list_roman[p][0]
                p += 1
            else:
                p += 1

        return res
            