class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        q = deque()
        
        # Left and right side Os
        for row in range(rows):
            if board[row][0]  == "O": 
                board[row][0] = "#"
                q.append((row, 0))
            if board[row][cols - 1] == "O": 
                board[row][cols - 1] = "#"
                q.append((row, cols - 1))

        # Top and bottom Os
        for col in range(cols):
            if board[0][col]  == "O": 
                board[0][col] = "#"
                q.append((0, col))
            if board[rows - 1][col] == "O": 
                board[rows - 1][col] = "#"
                q.append((rows - 1, col))

        # Run all BFS concurrently
        while q:
            r, c = q.popleft()

            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                # Guard against OOB, only go to "O"
                if (0 <= r + dr < rows and 0 <= c + dc < cols and 
                    board[r + dr][c + dc] == "O"):
                    board[r + dr][c + dc] = "#"
                    q.append((r + dr, c + dc))

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                if board[row][col] == "#":
                    board[row][col] = "O"


        
        
        # For each edge O, bfs through, any adjacent nodes, mark as # for safe
        # Pass through at the end and mark all X -> O, # -> X

