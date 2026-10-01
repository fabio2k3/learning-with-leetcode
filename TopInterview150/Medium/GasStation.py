class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalGas = sum(gas)
        totalCost = sum(cost)

        if totalGas < totalCost:
            return -1

        sumCost = 0
        start = 0

        for i in range(len(gas)):
            sumCost += gas[i] - cost[i]
            if sumCost < 0:
                sumCost = 0
                start = i + 1

        return start