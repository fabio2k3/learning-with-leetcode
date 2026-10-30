class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return 1
                
        p = 0

        res = 1

        while p < len(s):
            l = p -1
            r = p + 1
            if l > 0 and r < len(s):
                while l > 0 and r < len(s) and (s[l] == s[r]):
                    l -= 1
                    r += 1
                res = max(res, (r - l) + 1)
            p += 1

        p1 = 0
        p2 = 1

        while p1 < len(s) and p2 < len(s):
            l = p1 - 1
            r = p2 + 1

            if l > 0 and r < len(s):
                while l > 0 and r < len(s) and (s[l] == s[r]):
                    l -=1
                    r += 1

                res = max(res, (r - l) -1)