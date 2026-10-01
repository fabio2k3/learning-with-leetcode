class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        
        dic_mag = {}

        for i in range(len(magazine)):
            if magazine[i] not in dic_mag:
                dic_mag[magazine[i]] = 1
            else:
                dic_mag[magazine[i]] += 1

        for j in range(len(ransomNote)):
            if ransomNote[j] not in dic_mag:
                return False
            else:
                if dic_mag[ransomNote[j]] == 0:
                    return False
                else:
                    dic_mag[ransomNote[j]] -= 1


        return True