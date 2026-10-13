class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacificDrain, atlanticDrain = set(), set()

        def dfs(r, c, visited, prev):
            # Guard against OOB, upstream flows, or visited nodes
            if (r < 0 or c < 0 or r == rows or c == cols or
                heights[r][c] < prev or (r, c) in visited): 
                return
            visited.add((r, c))
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                dfs(r + dr, c + dc, visited, heights[r][c])

        for row in range(rows):
            dfs(row, 0, pacificDrain, heights[row][0])
            dfs(row, cols - 1, atlanticDrain, heights[row][cols - 1])
        for col in range(cols):
            dfs(0, col, pacificDrain, heights[0][col])
            dfs(rows - 1, col, atlanticDrain, heights[rows - 1][col])

        return [[r, c] for r, c in atlanticDrain & pacificDrain]
