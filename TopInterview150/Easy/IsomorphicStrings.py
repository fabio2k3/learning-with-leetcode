class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        lenS = len(s)
        lenT = len(t)

        dicS = {}
        dicT = {}

        if lenS != lenT:
            return False

        p = 0

        while p < lenS:
            if s[p] not in dicS:
                dicS[s[p]] = t[p]
            else:
                if dicS[s[p]] != t[p]:
                    return False

        p = 0
        
        while p < lenT:
            if t[p] not in dicS:
                dicT[t[p]] = s[p]
            else:
                if dicT[t[p]] != s[p]:
                    return False

        return True
        