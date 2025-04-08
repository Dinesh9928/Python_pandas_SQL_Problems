class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    

        for i in range(0, 9): # rows duplicate
            rowSet = set()
            for j in range(0, 9):
                if board[i][j] != ".":
                    if board[i][j] in rowSet:
                        return False
                rowSet.add(board[i][j])

        for i in range(0,9): # columns duplicates
            colSet = set()
            for j in range(0, 9):
                if board[j][i] != ".":
                    if board[j][i] in colSet:
                        return False
                    colSet.add(board[j][i])

        for row_box in range(3):
            for col_box in range(3):
                boxSet = set()
                for i in range(3):
                    for j in range(3):
                        r = row_box*3 +i
                        c = col_box*3 +j 
                        if board[r][c] == ".":
                            continue
                        if board[r][c] in boxSet:
                            return False
                        boxSet.add(board[r][c])
        return True
        
        

        