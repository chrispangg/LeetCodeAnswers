class TimeMap:

    def __init__(self):
        self.keyStore = {} #key: [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.keyStore.get(key, []) #use .get to get empty array if empty
        
        # Binary Search
        l,r = 0, len(values)
        while l < r:
            m = (l + r) // 2            
            if timestamp > values[m][1]:
                l = m + 1
            elif timestamp < values[m][1]:
                r = m
            else:
                return values[m][0]
        
        if not values or values[m][1] > timestamp:
            return ""
        else:
            return values[m][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

#10,20,30,40,50 target:31