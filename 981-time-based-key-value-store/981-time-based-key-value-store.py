class TimeMap:

    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.keyStore.get(key, [])
        
        if not values:
            return ""
        
        l,r = 0, len(values)
        
        while l < r:
            m = (l + r) // 2
            
            print("m:" + str(m))
            
            if timestamp > values[m][1]:
                l = m + 1
            elif timestamp < values[m][1]:
                r = m
            else:
                return self.keyStore[key][m][0]
        
        
        if self.keyStore[key][m][1] > timestamp:
            return ""
        else:
            return self.keyStore[key][m][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

#10,25,30,45,50,60 , target = 25
# l:0, r:5, m:3 , 10,25,30
# l:0, r:2, m:1 , 
