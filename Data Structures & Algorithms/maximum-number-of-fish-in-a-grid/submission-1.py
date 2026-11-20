class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        # ITERATIVE
        rows, cols = len(grid), len(grid[0])
        best = 0
        curr = 0

        s = []

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 0:
                    s.append((i, j))
                while s:
                    r, c = s.pop()
                    curr += grid[r][c]
                    # Mark as visited
                    grid[r][c] = 0

                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = r + dr, c + dc
                        # OOB and water with fish
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 0:
                            s.append((nr, nc))
                best = max(best, curr)
                curr = 0
        
        return best
                    
        
        
        # # RECURSIVE
        # rows, cols = len(grid), len(grid[0])
        # best = 0
        # curr = 0

        # def dfs(r: int, c: int) -> None:
        #     nonlocal curr
        #     curr += grid[r][c]

        #     # Mark as visited
        #     grid[r][c] = 0

        #     for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        #         nr, nc = r + dr, c + dc
        #         # OOB and water with fish
        #         if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 0:
        #             dfs(nr, nc)
                

        # for i in range(rows):
        #     for j in range(cols):
        #         # Land or visited 
        #         if grid[i][j] == 0:
        #             continue
        #         # Water with fish
        #         else:
        #             dfs(i, j)
        #             best = max(best, curr)
        #             curr = 0
        
        # return best


