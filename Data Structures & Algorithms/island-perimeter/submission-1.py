class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # For each peice of land:
        #   we want to count the total number of adjacent water cells
        #   append this to the total

        # if grid[i][j] is land:
        #   permiter += number of water adjacent

        # number of water adjacent: check any OOB, or 0 valued cells
        # Can use a for loop, need to visit every cell, only call this on land.
        # O(n*m) time, O(1) space. We run 4 checks max on every cell. n rows, m cols
        
        rows, cols = len(grid), len(grid[0])
        perimeter = 0

        def countBorder(r: int, c: int) -> int:
            cellPerimeter = 0

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                # Check if we're OOB, or in water
                if not (0 <= nr < rows) or not (0 <= nc < cols) or grid[nr][nc] == 0:
                    cellPerimeter += 1

            return cellPerimeter



        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1: # land
                    perimeter += countBorder(i, j)
        
        return perimeter


