class Solution:
    def totalNQueens(self, n: int) -> int:
        def es_seguro(tablero, fila, col, n):
            # Misma columna
            for i in range(fila):
                if tablero[i][col] == 1:
                    return False

            # Diagonal superior izquierda
            i, j = fila - 1, col - 1
            while i >= 0 and j >= 0:
                if tablero[i][j] == 1:
                    return False
                i -= 1
                j -= 1

            # Diagonal superior derecha
            i, j = fila - 1, col + 1
            while i >= 0 and j < n:
                if tablero[i][j] == 1:
                    return False
                i -= 1
                j += 1

            return True

        tablero = [[0] * n for _ in range(n)]
        contador = 0

        def backtrack(fila):
            nonlocal contador

            if fila == n:
                contador += 1
                return

            for col in range(n):
                if es_seguro(tablero, fila, col, n):
                    tablero[fila][col] = 1      # Colocar reina
                    backtrack(fila + 1)         # Siguiente fila
                    tablero[fila][col] = 0      # Retroceder

        backtrack(0)
        return contador