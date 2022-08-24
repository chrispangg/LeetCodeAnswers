"""
init small and large, maxheap and minheap respectively
addNum():
    - add to small always
    - if small[0] is larger than large[0], pop small push large
    - if len(small) > len(large) + 1: pop small push large
    - if len(large) > len(small) + 1: pop large push small
    

"""

class MedianFinder:

    def __init__(self):
        self.heaps = [], [] #small (maxheap) and large(minheap)

    def addNum(self, num: int) -> None:
        small, large = self.heaps
        heappush(small, -num)
        
        if small and large and -small[0] > large[0]:
            heappush(large, -heappop(small))
        if len(small) > len(large) + 1:
            heappush(large, -heappop(small))
        if len(large) > len(small) + 1:
            heappush(small, -heappop(large))
        
    def findMedian(self) -> float:
        small, large = self.heaps
        if len(small) > len(large):     return -small[0]
        elif len(small) < len(large):   return large[0]
        else:                           return (-small[0] + large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()