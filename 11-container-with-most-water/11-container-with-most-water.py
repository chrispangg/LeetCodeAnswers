"""
lines cannot be re-ordered
2 pointers
store area value. Area = min(two points)* distance(n[i] - n(j))
given example: height = [1,15,6,2,5,4,13,8,12] || 8, 96, 36
first loop:
i = 0
j = 9-1
num[i] = 1
num[j] = 7
Area = 8 * 1 = 8
store area value if larger than max
move logic: 
move the pointer that's giving the smallest value
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        l = 0
        r = len(height) - 1
        while l < r:
            area = min(height[l], height[r]) * (r-l)
            maxArea = max(maxArea, area)
            if(height[l] <= height[r]):
                l += 1
            else: 
                r -= 1
        return maxArea