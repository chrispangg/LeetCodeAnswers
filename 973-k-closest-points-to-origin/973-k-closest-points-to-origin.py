"""
minHeap - pop k number of values from a heap
distance from [0,0] = abs(x) + abs(y)
use map, where key = distance, value = coordinates
distance = sqrt(x^2 + y^2)
"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        heapq.heapify(distances)
        for x, y in points:
            distance = -(x**2 + y**2)
            if len(distances) == k:
                heapq.heappushpop(distances, [distance, x, y])
            else:
                heapq.heappush(distances, [distance, x, y])
        
        return [[x,y] for dist,x, y in distances]