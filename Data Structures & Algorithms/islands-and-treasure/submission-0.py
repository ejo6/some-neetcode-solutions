class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])

        q = deque()

        # Fill queue with treasure
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0: q.append((i, j, 0))

        while q:
            r, c, d = q.popleft()

            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                # Guard agains OOB, water, and already closer paths
                if (0 <= r + dr < rows and 0 <= c + dc < cols and
                    grid[r + dr][c + dc] != -1 and grid[r][c] + 1 < grid[r + dr][c + dc]):
                    grid[r + dr][c + dc] = d + 1
                    q.append((r + dr, c + dc, d + 1))


        # [(3, 0, 0), (1, 2, 1), (2, 0, 1)]



        # Start at top left, and iterate until we find treasure
        # Call a bfs() on the treasure and
        #   only traverse to cells where its distance to treasure can be improved
        #   update the cell with the new distance
        # Continue iterating, calling bfs each time we find treasure

