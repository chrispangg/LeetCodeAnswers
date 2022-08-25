class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        maxArea = 0
        
        def dfs(r, c):
            if (r < 0 or c < 0 or
                r >= row or c >= col or
               grid[r][c] == 0):
                return 0
            
            grid[r][c] = 0
            
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
            
            
        for r in range(row):
            for c in range(col):
                maxArea = max(maxArea, dfs(r, c))
        return maxArea