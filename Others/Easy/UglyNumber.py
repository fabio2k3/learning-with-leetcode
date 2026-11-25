class Solution:
    def isUgly(self, n: int) -> bool:
        if n % 2 == 0:
            return False
        
        n_copy = n

        while True:
            if n_copy % 5 == 0:
                n_copy //= 5

            elif n_copy % 3 == 0:
                n_copy //= 3

            elif n_copy % 2 == 0:
                n_copy //= 2
                
            else:
                break