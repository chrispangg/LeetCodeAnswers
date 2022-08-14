"""
nums: [1, 2, 3, 4]
pre:  [1, 1, 2, 6]
post: [24,12,4,1]
res:  [24,12,8,6]
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #prefix
        res = [1]
        for i in range(len(nums))[1:]:
            res.append(res[i-1] * nums[i-1])
        
        #postfix
        post = 1
        for i in range(len(nums))[::-1]:
            res[i] = res[i] * post
            post = post * nums[i]
        
        return res
        

