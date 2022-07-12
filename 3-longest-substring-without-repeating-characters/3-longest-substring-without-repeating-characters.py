"""
Sliding Window:
max = 0
set = ()

for-loop



if s[i+j] can be added to set, add to set and increment j if j < len[s]
else, compare max vs j, update max. i = i+j, set j = 0, 

Time: O(n); Space: O(n)
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = 0
        charSet = set()
        l = 0
        
        for r in range(len(s)):
            while s[r] in charSet: #if it's a duplicate, update our window
                charSet.remove(s[l]) #remove the left most value 
                l += 1
            
            charSet.add(s[r])
            res = max(res, len(charSet))
        return res