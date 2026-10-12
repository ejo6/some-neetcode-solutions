class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        
        def recurse(index: int, row: int, col: int) -> bool:
            # Base case: valid word
            if index == len(word) - 1: return True

            # Mark cell as explored (relies on our key assumption from earlier)
            temp = board[row][col]
            board[row][col] = '-'

            # Up
            if 0 <= row - 1 < rows and board[row - 1][col] == word[index + 1]:
                if recurse(index + 1, row - 1, col): return True

            # Down
            if 0 <= row + 1 < rows and board[row + 1][col] == word[index + 1]:
                if recurse(index + 1, row + 1, col): return True

            # Left
            if 0 <= col - 1 < cols and board[row][col - 1] == word[index + 1]:
                if recurse(index + 1, row, col - 1): return True

            # Right
            if 0 <= col + 1 < cols and board[row][col + 1] == word[index + 1]:
                if recurse(index + 1, row, col + 1): return True

            board[row][col] = temp 
            return False

        for i in range(rows):
            for j in range(cols):
                if board[i][j] != word[0]: continue
                # Check if this is a valid word
                if recurse(0, i, j): return True

        return False




        # Iterate from (0,0) until we see our first letter
        # Call if a neighbour is next letter, mark as explored, and recurse. 
        # Once we recurse onto the final letter, return true up the call stack
        
        # ! Key assumption: when we mark as "seen", it CANNOT be used in a valid solutiom

