class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def backtrack(actual, open, close):
            if len(actual) == 2 * n:
                res.append(actual)
                return

            if open < n:
                backtrack(actual + "(", open + 1, close)
            if close < open:
                backtrack(actual + ")", open, close + 1)

        backtrack("", 0, 0)
        return res