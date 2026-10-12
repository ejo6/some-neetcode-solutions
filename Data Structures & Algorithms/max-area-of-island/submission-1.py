class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0

        rows, cols = len(grid), len(grid[0])
        largestIsland = 0    

        # RECURSIVELY
        # def bfs(row: int, col: int) -> int:
        #     # We're OOB or in water
        #     if not (0 <= row < rows) or not (0 <= col < cols) or grid[row][col] == 0:
        #         return 0

        #     grid[row][col] = 0

        #     # Up + down + left + right
        #     return (bfs(row - 1, col) + 
        #             bfs(row + 1, col) +
        #             bfs(row, col - 1) +
        #             bfs(row, col + 1) + 1)

        def bfs(row: int, col: int) -> int:
            q = deque([(row, col)])
            grid[row][col] = 0
            area = 0

            while q:
                r, c = q.popleft()
                area += 1

                # Up
                if r - 1 >= 0 and grid[r - 1][c] == 1:
                    grid[r - 1][c] = 0
                    q.append((r - 1, c))
                # Down
                if r + 1 < rows and grid[r + 1][c] == 1:
                    grid[r + 1][c] = 0
                    q.append((r + 1, c))
                # Left
                if c - 1 >= 0 and grid[r][c - 1] == 1:
                    grid[r][c - 1] = 0
                    q.append((r, c - 1))
                # Right
                if c + 1 < cols and grid[r][c + 1] == 1:
                    grid[r][c + 1] = 0
                    q.append((r, c + 1))

            return area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    largestIsland = max(bfs(i, j), largestIsland)
        
        return largestIsland


