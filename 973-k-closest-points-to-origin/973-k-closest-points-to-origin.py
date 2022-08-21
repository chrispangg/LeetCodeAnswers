"""
minHeap - pop k number of values from a heap
distance from [0,0] = abs(x) + abs(y)
use map, where key = distance, value = coordinates
distance = sqrt(x^2 + y^2)
"""

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dic = {}
        distances = []
        res = []
        for point in points:
            distance = math.sqrt(point[0]**2 + point[1]**2)
            arr = dic.get(distance, [])
            arr.append(point)
            dic[distance] = arr
            distances.append(distance)
        
        heapq.heapify(distances)
        for i in range(k):
            p = dic[heapq.heappop(distances)]
            for r in p:
                res.append(r)

            if len(res) == k:
                break
        
        return res
        
        
        