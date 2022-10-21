class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        def dfs(r, c):
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                (r, c) in visited or 
                grid[r][c] == '0'):
                return 0
            
            visited.add((r, c))
            
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
            return 1
        
        res = 0
        for r in range(rows):
            for c in range(cols):
                    res += dfs(r, c)
        
        return res