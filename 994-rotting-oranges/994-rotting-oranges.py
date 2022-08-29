class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0: return -1

        rows, cols = len(grid), len(grid[0])
        res = 0
        
        def dfs(r, c, mins):
            # base case
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                grid[r][c] == 0 or 
                1 < grid[r][c] < mins):
                return 0
            
            grid[r][c] = mins
            
            dfs(r + 1, c, mins + 1)
            dfs(r - 1, c, mins + 1)
            dfs(r, c + 1, mins + 1)
            dfs(r, c - 1, mins + 1)
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    dfs(r, c, 2)

        res = 2
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: return -1
                res = max(res, grid[r][c])
        
        return res - 2