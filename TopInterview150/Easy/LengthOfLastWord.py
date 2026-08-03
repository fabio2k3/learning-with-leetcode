class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0

        n = len(s)

        if n == 0:
            return 0

        p = n - 1

        while p >= 0:
            if s[p] == " ":
                p -= 1
            else:
                while p >= 0 and s[p] != " ":
                    res += 1
                    p -= 1

                break

        return res