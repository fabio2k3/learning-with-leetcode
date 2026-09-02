class Solution:
    def mySqrt(self, x: int) -> int:
        res = 0

        p = 0

        if x == 0:
            return 0
        if x == 1:
            return 1
    
        while p <= (x // 2):
            if p*p == x:
                res = p
                break

            if p*p > x:
                res = p-1
                break

            res = p
            p += 1
            


        return res