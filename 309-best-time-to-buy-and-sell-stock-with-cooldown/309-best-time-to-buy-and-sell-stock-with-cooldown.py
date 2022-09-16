class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # State: Buying or Selling?
        # If Buy -> i + 1
        # If Sell -> i + 2

        cache = {}  # key=(i, buying) val=max_profit
        
        def dfs(i, buying):
            #buying is true means we can buy in this round
            if i >= len(prices): return 0
            if (i, buying) in cache : return cache[(i, buying)]
            
            cooldown = dfs(i+1, buying)
            if buying:
                buy = dfs(i+1, False) - prices[i]
                cache[(i, buying)] = max(buy, cooldown)
            else: #if buying is false
                sell = dfs(i+2, True) + prices[i]
                cache[(i, buying)] = max(sell, cooldown)
            return cache[(i, buying)]
        
        return dfs(0, True)