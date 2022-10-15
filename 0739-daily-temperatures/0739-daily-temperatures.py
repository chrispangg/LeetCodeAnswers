class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        minStack = [] #[i, temp]
        res = [0] * len(temperatures)
        
        for i, t in enumerate(temperatures):
            
            while len(minStack) > 0 and t > minStack[-1][1]:
                pos, temp = minStack.pop()
                res[pos] = i - pos
                
            minStack.append([i, t])
    
        return res
        