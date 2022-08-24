class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        if len(self.arr) % 2 == 1:
            i = len(self.arr) // 2
            self.arr.sort()
            return self.arr[i]
        else: # len(self.arr) % 2 == 0
            i = len(self.arr) // 2
            copy = self.arr.copy()
            copy.sort()
            return (copy[i - 1] + copy[i]) / 2
            
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()