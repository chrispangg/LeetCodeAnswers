class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        
        for i in range(k + 1):
            tmpPrices = prices.copy()
            
            for s, d, p in flights: #s=src, d=dst, p=price
                # infinity represents nodes we can't reach yet so we skip them
                if prices[s] == float("inf"): continue
                
                # if cost to src + price to dst < curr price to dst, then update
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
                
            prices = tmpPrices
        
        return -1 if prices[dst] == float("inf") else prices[dst]
    
                
                    
                