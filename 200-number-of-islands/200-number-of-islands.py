"""
Iterate through each of the cell and if it is an island, do dfs to mark all adjacent islands, then increase the counter by 1.
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        def dfs(r , c):
            if (r < 0 or c < 0 or 
                r >= len(grid) or c >= len(grid[0]) or 
                grid[r][c] != '1'):
                return
            
            grid[r][c] = '#'
            
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1':
                    dfs(r, c)
                    count += 1
        
        return count