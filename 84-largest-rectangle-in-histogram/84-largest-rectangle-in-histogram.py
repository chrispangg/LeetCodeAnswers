"""
Use a ascending monotonic stack to keep track index and height. 
When the stack is not empty adn it encounters a number smaller than the top of the stack, we pop the stack. 

As we pop, we calculates the local max and replace with maxArea if bigger. localmax can be calculated as such: height * (i - index), where index = stack's top's index. The differences is the width of what it could make

When we add to the stack, instead of putting the actual index, we put the index of where it could’ve extended to backwards.

Time and Space = O(N)

"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # pair: (index, height)
        
        
        for i, h in enumerate(heights):
            start = i
            
            # pop from stack if top stack's height is greater than h
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index #extend start index backwards
            
            stack.append((start, h))
        
        # for the remaining that was not popped from the stack
        # complete the caculation for the remaining values
        for i, h in stack:
            # the remaining can extend all the way to the end
            maxArea = max(maxArea, h * (len(heights) - i))
            
        return maxArea