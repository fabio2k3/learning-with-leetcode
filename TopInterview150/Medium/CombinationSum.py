class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()

        def backtrack(start: int, comb: list[int], remaining: int) -> None:
            if remaining == 0:
                res.append(comb.copy())
                return
            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                if candidates[i] > remaining:      
                    break
                comb.append(candidates[i])
                backtrack(i, comb, remaining - candidates[i])   
                comb.pop()

        backtrack(0, [], target)
        return res