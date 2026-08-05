class Solution:
    def reverseWords(self, s: str) -> str:
        lisWords = []

        n = len(s)

        p = 0

        while p < n:
            if s[p] != " ":
                word = ""
                while p < n and s[p] != " ":
                    word += s[p]
                    p += 1
                lisWords.append(word) 
            else:
                p += 1

        res = ""

        for i in range(len(lisWords) - 1, -1, -1):
            if i == 0:
                res += lisWords[i]
            else:
                res += lisWords[i] 
                res += " "

        return res

        