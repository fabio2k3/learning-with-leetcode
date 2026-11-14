class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        lx = [1, -1, 0, 0]
        ly = [0, 0, 1, -1]
        n = len(word)
        encontrada = False

        def backtrack(board, lx, ly, word, p, x, y):
            nonlocal encontrada          
            if encontrada:             
                return
            if p == len(word):
                encontrada = True
                return
            if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
                return
            if word[p] != board[x][y]:
                return

            temp = board[x][y]
            board[x][y] = '#'

            for i in range(len(lx)):
                nx = x + lx[i]
                ny = y + ly[i]
                backtrack(board, lx, ly, word, p + 1, nx, ny)   

            board[x][y] = temp

        for i in range(len(board)):
            for j in range(len(board[0])):
                backtrack(board, lx, ly, word, 0, i, j)
                if encontrada:
                    return True

        return encontrada

    c = "casa"

    print(c[-1])