class Solution:
    def simplifyPath(self, path: str) -> str:
        resPath = []

        for i in range(len(path)):
            if path[i] == ".":
                continue
            elif path[i] == "/" and (len(resPath) > 0 and resPath[0] == "/"):
                continue
            else:
                resPath.append(path[i])


        resStr = ""

        for element in resPath:
            resStr += element

        return resStr