class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordSet = set(wordDict)
        
        @lru_cache(None)
        def dfs(l):
            if l == n:
                return True
            
            r = l+1
            while r <= len(s):
                if s[l:r] in wordSet and dfs(r):
                    # print(s[l:r])
                    return True
                r+=1
            
            return False
        
        return dfs(0)
    