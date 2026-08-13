class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []

        n = len(s)

        if n == 0:
            return True
        if n == 1:
            return False

        p = 0

        while p < n:
            if len(myStack) == 0:
                myStack.append(s[p])
            else:
                val = s[p]
                if val == "(" or val == "{" or val == "[":
                    myStack.append(val)
                else:
                    if val == ")":
                        if myStack[-1] != "(":
                            return False
                        else:
                            myStack.pop()
                    elif val == "}":
                        if myStack[-1] != "{":
                            return False
                        else:
                            myStack.pop()
                    else:
                        if myStack[-1] != "[":
                            return False
                        else:
                            myStack.pop()

            p += 1

        if len(myStack) == 0:
            return True

        
        return False

            