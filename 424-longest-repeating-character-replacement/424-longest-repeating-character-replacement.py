"""
- 26 uppercase char, k operations max
Replace the char that matches the most common char in the window
WindowLen - count of the most frequrent character = remaining required
As long as remaining required is <= k, then it's a valid window
- Therefore: windowLen - most frequent char in window, and result is less than k = valid window
- Use a map to track most frequent in window
- expand the window (shift only right pointer) as long as the condition is valid. If not valid, we slide our window forward (shift left pointer)

Time Complexity: O(26n) -> O(n)
Space Complexity: 

"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        charMap = {}
        res = 0
        l = 0
        maxf = 0
        
        for r in range (len(s)):
            charMap[s[r]] = charMap.get(s[r], 0) + 1
            maxf = max(maxf, charMap[s[r]])
            
            if (r - l + 1) - maxf <= k: #valid window
                res = r - l + 1
            
            else: #invalid window
                if charMap[s[l]] == 0:
                    charMap[s[l]].pop(l)
                else:
                    charMap[s[l]] = charMap[s[l]] - 1
                l += 1
        
        return res
                
                
            
            
            
            
            
            
            
            
