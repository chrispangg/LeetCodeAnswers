class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        dp = {}
        def dfs(i, val):
            if (i, val) in dp: return dp[(i, val)]
            if i == k:
                if val == endPos: 
                    return 1
                else: 
                    return 0
            
            dp[(i, val)] = dfs(i + 1, val - 1) + dfs(i + 1, val + 1)
            
            return dp[(i, val)]
        
        return dfs(0, startPos) % (10**9 + 7)
