class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        level = [0]
        num = 0
        visited = set()
        while level:
            if amount in level:
                return num
            
            queue = []
            for a in level:
                for c in coins:
                    if a + c in visited: 
                        continue
                    if a + c <= amount:
                        queue.append(a+c)
                        visited.add(a+c)
                        
            level = queue
            num +=1
        
        return -1
            