class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        #prefix
        for i in range(1, len(nums)):
            res.append(res[i-1] * nums[i-1])
            
        #postfix
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * post
            post = post * nums[i]
        
        return res