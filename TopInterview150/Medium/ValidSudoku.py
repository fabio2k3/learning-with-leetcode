class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        lis_Pos =[False]*9


        filas = len(board)
        col = len(board[0])

        for i in range(filas):
            for j in range(col):
                if board[i][j] != ".":
                    val = int(board[i][j])
                    if lis_Pos[val-1]:
                        return False
                    else:
                        lis_Pos[val-1] = True

            lis_Pos = [False] * 9

        

        for j in range(col):
            for i in range(filas):
                if board[i][j] != ".":
                    val = int(board[i][j])
                    if lis_Pos[val-1]:
                        return False
                    else:
                        lis_Pos[val-1] = True

            lis_Pos = [False] * 9


        for i in range(0,3):
            for j in range(0,3):
                if board[i][j] != ".":
                    val = int(board[i][j])
                    if lis_Pos[val-1]:
                        return False
                    else:
                        lis_Pos[val-1] = True
                
        lis_Pos = [False] * 9


        for i in range(3,6):
            for j in range(0,3):
                if board[i][j] != ".":
                    val = int(board[i][j])
                    if lis_Pos[val-1]:
                        return False
                    else:
                        lis_Pos[val-1] = True
                        
        lis_Pos = [False] * 9


        for i in range(6,9):
            for j in range(0,3):
                if board[i][j] != ".":
                    val = int(board[i][j])
                    if lis_Pos[val-1]:
                        return False
                    else:
                        lis_Pos[val-1] = True
                                
        lis_Pos = [False] * 9



        for i in range(0,3):
            for j in range(3,6):
                if board[i][j] != ".":
                    val = int(board[i][j])
                    if lis_Pos[val-1]:
                        return False
                    else:
                        lis_Pos[val-1] = True
                                
        lis_Pos = [False] * 9



        for i in range(3,6):
            for j in range(3,6):
                if board[i][j] != ".":
                    val = int(board[i][j])
                    if lis_Pos[val-1]:
                        return False
                    else:
                        lis_Pos[val-1] = True
                                
        lis_Pos = [False] * 9



        for i in range(6,9):
            for j in range(3,6):
                if board[i][j] != ".":
                    val = int(board[i][j])
                    if lis_Pos[val-1]:
                        return False
                    else:
                        lis_Pos[val-1] = True
                                
        lis_Pos = [False] * 9



        for i in range(0,3):
            for j in range(6,9):
                if board[i][j] != ".":
                    val = int(board[i][j])
                    if lis_Pos[val-1]:
                        return False
                    else:
                        lis_Pos[val-1] = True
                                
        lis_Pos = [False] * 9



        for i in range(3,6):
            for j in range(6,9):
                if board[i][j] != ".":
                    val = int(board[i][j])
                    if lis_Pos[val-1]:
                        return False
                    else:
                        lis_Pos[val-1] = True
                                
        lis_Pos = [False] * 9


        for i in range(6,9):
            for j in range(6,9):
                if board[i][j] != ".":
                    val = int(board[i][j])
                    if lis_Pos[val-1]:
                        return False
                    else:
                        lis_Pos[val-1] = True
                                
        lis_Pos = [False] * 9

        return True