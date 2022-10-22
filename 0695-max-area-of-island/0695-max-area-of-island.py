class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxSize = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                (r, c) in visited or 
                grid[r][c] == 0):
                return 0
            
            visited.add((r, c))
            
            size = dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
            
            return 1 + size
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    size = dfs(r, c)
                    maxSize = max(maxSize, size)
        
        return maxSize