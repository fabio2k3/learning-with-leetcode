class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0

        es_primo = [True] * n
        es_primo[0] = es_primo[1] = False

        for p in range(2, int(n ** 0.5) + 1):
            if es_primo[p]:
                es_primo[p * p : n : p] = [False] * (((n - 1 - p * p) // p) + 1)

        return sum(es_primo)

            