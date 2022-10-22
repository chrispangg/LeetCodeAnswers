class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def dfs(r, c, visited, prevHeight):
            if ((r, c) in visited or
                r < 0 or c < 0 or
                r >= rows or c >= cols or
                heights[r][c] < prevHeight):
                return
            
            height = heights[r][c]    

            visited.add((r, c))
            dfs(r + 1, c, visited, height)
            dfs(r - 1, c, visited, height)
            dfs(r, c + 1, visited, height)
            dfs(r, c - 1, visited, height)
            
        for c in range(cols):
            dfs(0, c, pac, heights[0][c]) #top pac
            dfs(rows-1, c, atl, heights[rows-1][c]) #bot atl
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0]) #left pac
            dfs(r, cols-1, atl, heights[r][cols-1]) #right atl
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res