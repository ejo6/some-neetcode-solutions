class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0

        rows, cols = len(grid), len(grid[0])
        largestIsland = 0    
    
        def bfs(row: int, col: int) -> int:
            # We're OOB or in water
            if not (0 <= row < rows) or not (0 <= col < cols) or grid[row][col] == 0:
                return 0

            grid[row][col] = 0

            # Up + down + left + right
            return (bfs(row - 1, col) + 
                    bfs(row + 1, col) +
                    bfs(row, col - 1) +
                    bfs(row, col + 1) + 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    largestIsland = max(bfs(i, j), largestIsland)
        
        return largestIsland