class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = {} # (r, c) -> LIP
        
        def dfs(r, c, prevVal):
            # base case 1: 
            if(r < 0 or c < 0 or # out of bound
               r >= rows or c >= cols or # out of bound
               prevVal >= matrix[r][c]): # smaller val than prevVal
                return 0
            
            # base case 2: return cache
            if (r, c) in dp: 
                return dp[(r, c)]
            
            #check all four positions and self for max
            dp[(r, c)] = max(1, 
                      1+dfs(r-1, c, matrix[r][c]),
                      1+dfs(r+1, c, matrix[r][c]),
                      1+dfs(r, c-1, matrix[r][c]),
                      1+dfs(r, c+1, matrix[r][c])
                     )
            return dp[(r, c)]
            
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, -1)
        
        return max(dp.values())
            
        
            
            