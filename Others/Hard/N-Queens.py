class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        def es_seguro(tablero, fila, col, n):
            for i in range(fila):
                if tablero[i][col] == 1:
                    return False

            i, j = fila - 1, col - 1
            while i >= 0 and j >= 0:
                if tablero[i][j] == 1:
                    return False
                i -= 1
                j -= 1

            i, j = fila - 1, col + 1
            while i >= 0 and j < n:
                if tablero[i][j] == 1:
                    return False
                i -= 1
                j += 1

            return True

        tablero = [[0] * n for _ in range(n)]
        soluciones = []

        def backtrack(fila):
            if fila == n:
                soluciones.append([
                    ''.join('Q' if tablero[i][j] == 1 else '.' for j in range(n))
                    for i in range(n)
                ])
                return

            for col in range(n):
                if es_seguro(tablero, fila, col, n):
                    tablero[fila][col] = 1
                    backtrack(fila + 1)
                    tablero[fila][col] = 0

        backtrack(0)
        return soluciones