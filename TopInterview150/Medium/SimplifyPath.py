class Solution:
    def simplifyPath(self, path: str) -> str:
        dicLetters = {'a': 1,
            'b': 1,
            'c': 1,
            'd': 1,
            'e': 1,
            'f': 1,
            'g': 1,
            'h': 1,
            'i': 1,
            'j': 1,
            'k': 1,
            'l': 1,
            'm': 1,
            'n': 1,
            'o': 1,
            'p': 1,
            'q': 1,
            'r': 1,
            's': 1,
            't': 1,
            'u': 1,
            'v': 1,
            'w': 1,
            'x': 1,
            'y': 1,
            'z': 1,  
            'A': 1,
            'B': 1,
            'C': 1,
            'D': 1,
            'E': 1,
            'F': 1,
            'G': 1,
            'H': 1,
            'I': 1,
            'J': 1,
            'K': 1,
            'L': 1,
            'M': 1,
            'N': 1,
            'O': 1,
            'P': 1,
            'Q': 1,
            'R': 1,
            'S': 1,
            'T': 1,
            'U': 1,
            'V': 1,
            'W': 1,
            'X': 1,
            'Y': 1,
            'Z': 1, }

        words_list = []
        i = 0

        while i < len(path):
            if path[i] in dicLetters:
                word = ""
                while i < len(path) and path[i] in dicLetters:
                    word += path[i]
                    i += 1
                words_list.append(word)
            elif path[i] == '.':
                count = 0
                while i < len(path) and path[i] == '.':
                    count += 1
                    i += 1
                if count == ""

            i += 1

        n = len(words_list)
        res = "/"

        for j in range(n):
            if words_list[j] == "Documents":
                continue
            if j == n - 1:
                res += words_list[j]
            else:
                res += words_list[j] + "/"

        return res