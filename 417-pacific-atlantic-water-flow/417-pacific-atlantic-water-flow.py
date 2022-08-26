class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        row, col = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def dfs(r, c, visit, prevHeight):
            
            
            if((r,c) in visit or
               r < 0 or
               c < 0 or
               r >= row or
               c >= col or
               heights[r][c] < prevHeight): #if prevHeight is larger, than it woudn't reach the edge
                return 
            
            height = heights[r][c]
            
            visit.add((r,c))
            dfs(r + 1, c, visit, height)
            dfs(r - 1, c, visit, height)
            dfs(r, c + 1, visit, height)
            dfs(r, c - 1, visit, height)
            
        for c in range(col):
            dfs(0, c, pac, heights[0][c]) #from top pacific edge
            dfs(row - 1, c, atl, heights[row - 1][c]) #from bottom atlantic edge 
        
        for r in range(row):
            dfs(r, 0, pac, heights[r][0]) #from left pacific edge
            dfs(r, col - 1, atl, heights[r][col - 1]) #from right atlantic edge 
        
        res = []
        for r in range(row):
            for c in range(col):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        
        return res
            
            
            
            
            
            