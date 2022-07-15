"""
Sliding Window Question: Key is we always want to start again from the lowest known number
    - So move left pointer to the smallest known number
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, l = 0, 0
        
        for r in range(len(prices)):
            if prices[r] - prices[l] > res:
                res = max(res, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
        
        return res
