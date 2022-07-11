"""
track max height of both side
take the min height of the maxes
min of max height * value - value
move the smaller point on loop
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height: return 0
        
        res = 0 
        l,r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        
        while l < r:
            if leftMax < rightMax: #shift left pointer
                l += 1
                leftMax = max(leftMax, height[l]) #compare and update leftMax
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r]) #compare and update rightMax
                res += rightMax - height[r]
        return res
                