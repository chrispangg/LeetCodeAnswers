class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        i = len(self.arr) // 2
        self.arr.sort()
        if len(self.arr) % 2 == 1:
            return self.arr[i]
        else:
            return (self.arr[i - 1] + self.arr[i]) / 2
            
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()