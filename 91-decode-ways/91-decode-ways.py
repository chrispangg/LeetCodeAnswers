class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {len(s):1} #if empty string return 1
        def dfs(i):
            # base case 1: if cached or reached end of string 
            if i in cache:
                return cache[i]
            if s[i] == "0":
                return 0
            
            res = dfs(i + 1)
            
            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                res += dfs(i + 2)
            
            cache[i] = res
            
            return res
        
        return dfs(0)
        