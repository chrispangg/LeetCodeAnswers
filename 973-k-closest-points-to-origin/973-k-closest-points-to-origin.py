"""
minHeap - pop k number of values from a heap
distance from [0,0] = abs(x) + abs(y)
use map, where key = distance, value = coordinates
distance = sqrt(x^2 + y^2)
"""

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for point in points:
            distance = math.sqrt(point[0]**2 + point[1]**2)
            distances.append([distance, point[0], point[1]])
        
        heapq.heapify(distances)
        
        res = []
        for i in range(k):
            distance, x, y = heapq.heappop(distances)
            res.append([x, y])
        
        return res
        
        
        