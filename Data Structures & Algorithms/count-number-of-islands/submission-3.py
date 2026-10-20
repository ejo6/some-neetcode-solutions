class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Iterate through until we find land
        # DFS down that island, marking nodes as water so we don't visit again
        # After the dfs finished, incrament our island counter and continue

        numIslands = 0
        rows, cols = len(grid), len(grid[0])
        s = []

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    s.append((i, j))
                    
                    while s:
                        r, c = s.pop()
                        grid[r][c] = '0'

                        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            if (0 <= r + dr < rows) and (0 <= c + dc < cols) and grid[r + dr][c + dc] == '1':
                                s.append((r + dr, c + dc))
                    numIslands += 1
        
        return numIslands