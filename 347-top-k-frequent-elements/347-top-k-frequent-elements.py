"""
Bubble sort, where index = frequency and val = the number
pop from the back until we got two values
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #Hashmap
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
            
        #Create bucket
        bucket = []
        for i in range(len(nums) + 1):
            bucket.append(None)
        
        #Generate bucket
        for key in dic: 
            if bucket[dic[key]] == None:
                l = []
                l.append(key)
                bucket[dic[key]] = l
            else:   
                bucket[dic[key]].append(key)
                        
        #Generate result
        res = []
        for i in range(len(nums)):
            r = bucket.pop()
            if r is not None:
                while r and len(res) < k:
                    val = r.pop()
                    res.append(val)
        
        return res