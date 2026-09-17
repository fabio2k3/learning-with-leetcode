class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        resultado = 1.0

        while n > 0:
            if n % 2 == 1:
                resultado *= x

            x *= x
            n //= 2

        return resultado