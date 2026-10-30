class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        res = s[0]
        n = len(s)

        p = 0
        while p < n:
            l = p - 1
            r = p + 1

            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1

            if r - (l + 1) > len(res):
                res = s[l + 1:r]

            p += 1

        p1 = 0
        p2 = 1

        while p2 < n:
            l = p1
            r = p2

            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1

            if r - (l + 1) > len(res):
                res = s[l + 1:r]

            p1 += 1
            p2 += 1

        return res