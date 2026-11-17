class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n % 2 == 0:
            return False
        if n == 1:
            return True
        
        n_c = n

        while n_c % 3 == 0 and n_c > 1:
            n_c //= 3

            if n_c % 2 == 0:
                return False

        if n_c == 1:
            return True
        else:
            return False