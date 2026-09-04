class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)

        if n == 1:
            return strs[0]
        
        minLength = len(strs[0])
        for string in strs:
            if len(string) == 0:
                return ""
            if len(string) < minLength:
                minLength = len(string)

        res = ""
        finish = False
        for i in range(minLength):
            c = strs[0][i]
            for j in range(1,n):
                if strs[j][i] != c:
                    finish = True
                    break
                else:
                    continue
            if finish:
                break
            res += c

        return res