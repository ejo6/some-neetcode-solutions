class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(row: int, col: int) -> None:
            q = deque([(row, col)])
            grid[row][col] = '0' # mark visited

            while q:
                r, c = q.popleft()

                # Up
                if r - 1 >= 0 and grid[r - 1][c] == '1':
                    grid[r - 1][c] = '0'
                    q.append((r - 1, c))
                # Down
                if r + 1 < rows and grid[r + 1][c] == '1':
                    grid[r + 1][c] = '0'
                    q.append((r + 1, c))
                # Left
                if c - 1 >= 0 and grid[r][c - 1] == '1':
                    grid[r][c - 1] = '0'
                    q.append((r, c - 1))
                # Right
                if c + 1 < cols and grid[r][c + 1] == '1':
                    grid[r][c + 1] = '0'
                    q.append((r, c + 1))

            return

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    islands += 1
                    bfs(i, j)

        return islands


