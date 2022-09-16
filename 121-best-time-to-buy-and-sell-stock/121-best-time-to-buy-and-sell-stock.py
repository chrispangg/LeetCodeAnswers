"""
Sliding Window technique
Look for the next smallest value, while keeping track our max profit

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,0
        res = 0
        for r in range(len(prices)):
            res = max(res, prices[r] - prices[l])
            
            if prices[r] < prices[l]:
                l = r
        return res
        
            