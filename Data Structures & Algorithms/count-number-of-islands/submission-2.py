class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Iterate through until we find land
        # DFS down that island, marking nodes as water so we don't visit again
        # After the dfs finished, incrament our island counter and continue

        numIslands = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> None:
            nonlocal numIslands

            grid[r][c] = '0'

            # Call each adjacent node
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if (0 <= r + dr < rows) and (0 <= c + dc < cols) and grid[r + dr][c + dc] == '1':
                    dfs(r + dr, c + dc)


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    dfs(i, j)
                    numIslands += 1
        
        return numIslands