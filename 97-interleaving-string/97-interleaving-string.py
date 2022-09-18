class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        row, col = len(s1), len(s2)
        dp = [[False]* (col + 1) for i in range(row + 1)]
        dp[row][col] = True 
        
        
        #each element on each row (so col first)
        for r in range(row, -1, -1):
            for c in range(col, -1, -1):
                #look right one cell and look left one cell
                if r < len(s1) and s1[r] == s3[r + c] and dp[r + 1][c]:
                    dp[r][c] = True
                if c < len(s2) and s2[c] == s3[r + c] and dp[r][c + 1]:
                    dp[r][c] = True
        
        return dp[0][0]
                
