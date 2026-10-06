class Solution:
    def reverse(self, x: int) -> int:
        if -10 < x < 10:
            return x
        
        lim_min = (2**31) * (-1)
        lim_max = 2**31 - 1

        if x <= lim_min or x >= lim_max:
            return 0

        x_str = str(x)

        num = ""

        if x < 0:
            num = x_str[1:]
        else:
            num = x_str

        l = 0
        r = len(num) - 1

        lista = list(num)

        while l < r:
            lista[l], lista[r] = lista[r], lista[l]

            l += 1
            r -= 1

        if lista[0] == "0":
            lista.pop(0)

        res = int(''.join(lista))
        
        if res < lim_min or res > lim_max:
            return 0

        if x < 0:
            return res*(-1)
        else:
            return res

        