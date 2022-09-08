class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        def findSubstring(l, r):
            subRes = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                subRes += 1
                l -= 1
                r += 1
            return subRes
        
        for i in range(len(s)):
            res += findSubstring(i,i) + findSubstring(i,i+1)
            
        return res