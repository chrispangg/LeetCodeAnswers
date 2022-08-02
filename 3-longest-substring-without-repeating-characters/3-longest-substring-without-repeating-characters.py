"""
Sliding Window + set
if not repeated add value to set
if repeated, remove the left most char until it's not no longer repeated
track largest size as we cycle
return res
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        res = 0
        l = 0
        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1

            chars.add(s[r])
            res = max(res, len(chars))
                
        return res