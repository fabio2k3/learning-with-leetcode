class Solution:
    def isPalindrome(self, s: str) -> bool:
        wordCheck = ""

        p = 0

        n = len(s)

        if n == 0:
            return True

        dic = {chr(i): 1 for i in range(ord('a'), ord('z')+1)}

        for i in range(10):
            numStr = str(i)
            dic[numStr] = 1

        while p < n:
            myChar = s[p]
            charCheck = myChar.lower()

            if charCheck not in dic:
                p += 1
            else:
                wordCheck += charCheck
                p += 1


        if len(wordCheck) == 1:
            return True

        l = 0
        r = len(wordCheck) - 1

        while l < r:
            if wordCheck[l] != wordCheck[r]:
                return False

            l += 1
            r -= 1

        return True

            

