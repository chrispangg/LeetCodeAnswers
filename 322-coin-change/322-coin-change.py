class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [float('inf')] * (amount + 1) # 0...amount
        cache[0] = 0
        
        for a in range(amount + 1):
            for c in coins:
                if a - c >= 0:
                    """
                    coin = 4, a = 7
                    cache[7] = 1 + cache[7-4]
                    """
                    cache[a] = min(cache[a], 1 + cache[a - c])
        
        return cache[amount] if cache[amount] != float('inf') else -1