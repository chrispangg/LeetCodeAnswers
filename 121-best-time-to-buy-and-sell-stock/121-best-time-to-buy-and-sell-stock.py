"""
Sliding Window. Keep track of buy price, sell price and profit. The key is to relocate buy and sell pointers to the lowest known value, then move sell pointer forward, WHILE we keep track of the max profit before the relocation
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = 0 #left
        s = 1 #right
        p = 0
        while s < len(prices):
            if prices[b] < prices[s]:
                p = max(p, prices[s] - prices[b])
            else:
                # b += 1
                b = s
            s += 1
        return p

# Time Complexity: O(n)
# Space Complexity: O(1)

