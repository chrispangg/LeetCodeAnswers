# HashMap, where key = target-num and value = pos in array - num i.e. 7:1 for the first value in the array
# for-loop
    # if hashmap has key 7, then get value and put that into the first array box
    # then put arr[i] into the second array box
# Time Complexity = O(n)
# Space Complexity = O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        hashMap = {}
        res = []
        
        for i, number in enumerate(numbers):
            reminder = target - number
            
            if(number in hashMap):
                res.append(hashMap.get(number))
                res.append(i + 1)
                return res
            else:
                hashMap[reminder] = i + 1
        return res
    