class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {len(s):1} #if empty string return 1
        def dfs(i):
            # base case 1: if cached or reached end of string 
            if i in cache:
                print("it's in cache: " + str(i))
                return cache[i]
            # base case 2: if we see a 0, it means branch is invalid
            if s[i] == "0": return 0
            
            res = dfs(i + 1)
            
            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                res += dfs(i + 2)
            
            print("i: " + str(i) + " res: " + str(res))
            cache[i] = res
            
            return res
        
        return dfs(0)