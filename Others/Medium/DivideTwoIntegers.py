class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        n1 = abs(dividend)
        n2 = abs(divisor)

        res = 0

        while n1 >= n2:
            multi = n2
            count = 1

            while n1 >= multi + multi:
                multi += multi
                count += count

            n1 -= multi
            res += count


        if (dividend < 0) != (divisor < 0):
            return -res
        else:
            return min(max(res, -2**31), 2**31 - 1)