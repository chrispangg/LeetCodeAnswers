class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        visited = set()
        level = [0]
        num = 0
        while level:
            if amount in level: return num
            
            queue = []
            for l in level:
                for c in coins:
                    if c + l <= amount and (c + l) not in visited:
                        queue.append(c + l)
                        visited.add(c + l)
            num += 1
            level = queue
        return -1
                    
        
        
            