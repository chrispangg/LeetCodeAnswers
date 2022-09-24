class Solution:
    def jump(self, nums: List[int]) -> int:
        l,r = 0,0
        res = 0
        
        """
        On every loop, set L pointer to R pointer + 1
        set R pointer to the furthest we can go
        """
        while r < (len(nums) - 1):
            newR = r
            for i in range(l, r+1):
                newR = max(newR, i + nums[i])
            
            l = r + 1
            r = newR
            res += 1
        return res
            
            