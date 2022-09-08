class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_l, res_r = 0, 0
        resLen = 0
        
        for i in range(len(s)):
            # check for odd palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res_r, res_l = r + 1, l
                    resLen = r - l + 1
                l -= 1
                r += 1
            
            # check for even palindromes
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res_r, res_l = r + 1, l
                    resLen = r - l + 1
                l -= 1
                r += 1
            
        print(str(res_l) + " " + str(res_r))
        return s[res_l: res_r]