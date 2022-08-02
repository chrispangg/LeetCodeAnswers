"""
num[i] starts at where the left pointer is at and increment when all three numbers = 0
left right pointers - starting from left and right, where left = i + 1 and right = len(num) - 1
increment left pointer if it's less than 0
decrement right pointer if it's more than 0
save them in a set to avoid duplicates
end the loop when l<r is not valid

"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        
        for i, num in enumerate(nums):
            l,r = i+1, len(nums)-1
            
            if l == r:
                break
            
            while l < r:
                threeSum = num + nums[l] + nums[r]
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    res.add(tuple([num, nums[l], nums[r]]))
                    l += 1
            
            
            
        return list(res)