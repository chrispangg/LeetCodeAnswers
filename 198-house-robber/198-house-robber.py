class Solution:
    def rob(self, nums: List[int]) -> int:
        rob, notRob = 0, 0
        
        for n in nums:
            temp = max(rob + n, notRob)
            rob = notRob
            notRob = temp
        
        return notRob