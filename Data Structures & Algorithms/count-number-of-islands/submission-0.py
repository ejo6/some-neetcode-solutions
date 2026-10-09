class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0': 
                    continue
                self.searchLand(i, j, grid)
                numIslands += 1

        return numIslands

    
    def searchLand(self, i: int, j: int, grid: List[List[str]]):
        if (i < 0) or (i >= len(grid)) or (j < 0) or (j >= len(grid[0])) or grid[i][j] == '0':
            return 

        grid[i][j] = '0'

        self.searchLand(i - 1, j, grid)
        self.searchLand(i + 1, j, grid)
        self.searchLand(i, j - 1, grid)
        self.searchLand(i, j + 1, grid)




    # ["1","1","0","0","1"],
    # ["1","1","0","0","1"],
    # ["0","0","1","0","0"],
    # ["0","0","0","1","1"]

        # 1. Iterate through the list (for i, for j) and once we find land, goto 2

        # 2. recursively check if the neighbours are land/found, mark as found
            # a. when marking as found, 0 workds as well, since it's area we want to ignore (so long as we can modify the input)
            # b. if the area is out of bounds, (i, j< 0, j >= len(grid[0]), i < len(grid)), not not compute.
        # 3. once theres not land left on the island, incrament the island counter and go back to step 1.

        # 4. Once we're at the end of the array, return the island counter

