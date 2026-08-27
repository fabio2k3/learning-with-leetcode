class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x < 10:
            return True

        numStr = str(x)

        n = len(numStr)

        l, r = 0, n - 1

        while l < r:
            if numStr[l] != numStr[r]:
                return False
            l += 1
            r -= 1

        return True