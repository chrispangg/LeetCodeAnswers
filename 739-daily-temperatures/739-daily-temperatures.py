"""
Use a decreasing stack to keep track of the lowest temp
Pop the stack when it encounter a higher value

Time: O(N)
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #pair: [temp, index], add index for calculating the num of days to find a higher temp
        
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: #stack[-1][0] gets the temp
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd #diff between current temp and the next lowest temp
            stack.append([t,i])
        return res