class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        freshFruit = 0
        q = deque() # track: (row, col, minute)
        finalMinute = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: freshFruit += 1
                elif grid[r][c] == 2: q.append((r, c, 0))


        # BFS from each rotten:
        while q:
            r, c, m = q.popleft()
            finalMinute = max(finalMinute, m)

            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                # Guard against OOB, already rotten, empty cells
                if ((0 <= r + dr < rows) and (0 <= c + dc < cols) and
                    grid[r + dr][c + dc] != 2 and grid[r + dr][c + dc] != 0):
                    # Rotten and append a fruit, incrament counter
                    grid[r + dr][c + dc] = 2
                    freshFruit -= 1
                    q.append((r + dr, c + dc, m + 1))

        if freshFruit > 0: return -1
        return finalMinute
    

        # BFS from each rotten fruit (figure out the indices first),
        # Track the number of remaining fruit
        # DO NOT iterate through already rotten fruit
        # We need to track each time a minute passed (track the current length of the queue, once its empty, that was a full minute)

