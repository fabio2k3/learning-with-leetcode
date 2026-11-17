class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        fibArr = [0]*(n+1)

        fibArr[1] = 1

        for i in range(2, n + 1):
            fibArr[i] = fibArr[i - 1] + fibArr[i - 2]

        return fibArr[-1]