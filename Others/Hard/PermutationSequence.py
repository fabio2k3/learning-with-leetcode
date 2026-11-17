from math import factorial
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        arr = []
        for num in range(1, n + 1):
            arr.append(num)

        k -= 1
        res = []

        for i in range(n, 0 , -1):
            fact = factorial(i - 1)
            index = k // fact
            k = k % fact
            res.append(arr.pop(index))

        return ''.join(map(str, res))