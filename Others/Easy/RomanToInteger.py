class Solution:
    def romanToInt(self, s: str) -> int:
        dic_ri = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        if len(s) == 1:
            return dic_ri[s[0]]

        p = 0

        res = 0

        while p < len(s):
            if p+1 < len(s) and (dic_ri[s[p+1]] > dic_ri[s[p]]):
                res += dic_ri[s[p+1]] - dic_ri[s[p]]
                p += 2
            else:
                res += dic_ri[s[p]]
                p += 1

        return res
