class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_S = len(s)
        len_t = len(t)

        if len_S > len_t:
            return False

        if len_S == 0:
            return True

        pS = 0
        pT = 0 

        while pT < len_t:
            if s[pS] == t[pT]:
                pS += 1
                if pS == len_S:
                    return True
            pT += 1

        return False