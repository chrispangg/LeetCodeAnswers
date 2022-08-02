"""
nums to set

if set contains n-1, we skip
if set does not contain n-1, we can increment forward, and remove() n-1 from set
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nSet = set(nums)
        
        for n in nums:
            if n-1 in nSet:
                continue
            else:
                curr, temp = n, 0
                while curr in nSet:
                    temp += 1
                    res = max(res, temp)
                    curr += 1
                    
        return res