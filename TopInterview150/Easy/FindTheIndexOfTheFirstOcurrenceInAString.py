class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ph = 0
        nh = len(haystack)

        pn = 0
        nn = len(needle)

        if nn > nh:
            return -1
        if nn == nh:
            if haystack == needle:
                return 0
            else:
                return -1

        while ph < nh:
            if haystack[ph] == needle[pn]:
                count = 0
                res = ph
                ph_copy = ph
                while ph_copy < nh and pn < nn and haystack[ph_copy] == needle[pn]:
                    count += 1
                    ph_copy += 1
                    pn += 1
                if count == nn:
                    return res
                else:
                    pn = 0
            ph += 1

        return -1
