"""
minHeap - pop k number of values from a heap
distance from [0,0] = abs(x) + abs(y)
use map, where key = distance, value = coordinates
distance = sqrt(x^2 + y^2)
"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for x, y in points:
            distance = sqrt(x **2 + y **2)
            distances.append([distance, x, y])
        
        heapq.heapify(distances)
        
        res = []
        for i in range(k):
            distance, x, y = heapq.heappop(distances)
            res.append([x, y])
        
        return res