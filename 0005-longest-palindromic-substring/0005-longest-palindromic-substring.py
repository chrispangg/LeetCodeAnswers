class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = 0
        
        
        for i in range(len(s)):
            
            #for odd length string
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > res:
                    res = r - l + 1
                    res_l = l
                    res_r = r + 1
                l -= 1
                r += 1
            
            #for even length string
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > res:
                    res = r - l + 1
                    res_l = l
                    res_r = r + 1
                l -= 1
                r += 1
        
        return s[res_l:res_r]