class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (self.checkRows(board) 
                and self.checkCols(board) 
                and self.checkSquares(board))

    def checkRows(self, board: List[List[str]]) -> bool:
        vals = [0] * 9
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".": continue # nothing at this val
                vals[int(board[i][j]) - 1] += 1
                # Check if multiple found in area
                if vals[int(board[i][j]) - 1] > 1:
                    return False
            vals = [0] * 9
        return True

    def checkCols(self, board: List[List[str]]) -> bool:
        vals = [0] * 9
        for i in range(9):
            for j in range(9):
                if board[j][i] == ".": continue # nothing at this val
                vals[int(board[j][i]) - 1] += 1
                # Check if multiple found in area
                if vals[int(board[j][i]) - 1] > 1:
                    return False
            vals = [0] * 9
        return True

    def checkSquares(self, board: List[List[str]]) -> bool:
        for i in range(0,9,3):
            for j in range(0,9,3):
                if not self.checkSquaresHelper(j, i, board): return False
        return True

    def checkSquaresHelper(self, x: int, y: int, board: List[List[str]]) -> bool:
        vals = [0] * 9
        for i in range(x,x+3):
            for j in range(y,y+3):
                if board[i][j] == ".": continue # nothing at this val
                vals[int(board[i][j]) - 1] += 1
                # Check if multiple found in area
                if vals[int(board[i][j]) - 1] > 1:
                    return False
        return True
    




