class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:


        def eliminateIsland(row, col):
            nonlocal grid
            if grid[row][col] == "0":
                return
            
            grid[row][col] = "0"
            dir = [(0,1), (0, -1), (1, 0), (-1, 0)]

            for dr, dc in dir:
                if 0 <= dr + row < len(grid) and 0 <= dc + col < len(grid[0]):
                    eliminateIsland(row + dr, col + dc)
            
            return
            
        
        res = 0
        if not grid or not grid[0]:
            return 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    eliminateIsland(r, c)
                    res += 1
        
        return res
