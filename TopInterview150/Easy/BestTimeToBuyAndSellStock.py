class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxNum = prices[-1]
        n = len(prices)

        maxArray = [0]*n

        maxArray[-1] = maxNum

        for i in range(n-2, -1, -1):
            if prices[i] > maxNum:
                maxNum = prices[i]
            maxArray[i] = maxNum

        res = 0

        for i in range(n):
            if maxArray[i] - prices[i] > res:
                res = maxArray[i] - prices[i]

        return res