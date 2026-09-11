class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def create_combinations(lis, n, k, comb, start):
            if len(comb) == k:
                lis.append(comb.copy())
                return

            for i in range(start, n + 1):
                comb.append(i)
                create_combinations(lis, n, k, comb, i + 1)
                comb.pop()

        lis = []
        create_combinations(lis, n, k, [], 1)

        return lis