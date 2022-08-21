class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.maxheap = [-1 * i for i in stones]
        print(self.maxheap)
        heapify(self.maxheap)
        
        while len(self.maxheap) > 1:
            y = -1 * heapq.heappop(self.maxheap)
            x = -1 * heapq.heappop(self.maxheap)
            
            val = y - x
            if val > 0:
                heapq.heappush(self.maxheap, -1 * val)
        
        return -1 * self.maxheap[0] if self.maxheap else 0
        