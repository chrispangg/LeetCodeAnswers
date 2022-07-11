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