class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicS = {}

        for c in s:
            if c not in dicS:
                dicS = 1
            else:
                dicS[c] += 1

        for c in t:
            if c not in dicS:
                return False
            else:
                if dicS[c] == 0:
                    return False
                else:
                    dicS[c] -= 1

        return True