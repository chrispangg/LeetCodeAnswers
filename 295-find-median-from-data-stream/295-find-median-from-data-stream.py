class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        i = len(self.arr) // 2
        if len(self.arr) % 2 == 1:
            self.arr.sort()
            return self.arr[i]
        else: # len(self.arr) % 2 == 0
            self.arr.sort()
            return (self.arr[i - 1] + self.arr[i]) / 2
            
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()