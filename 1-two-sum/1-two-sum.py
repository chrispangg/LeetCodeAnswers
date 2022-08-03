class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        res = []
        
        for i in range(len(nums)):
            
            if nums[i] in dic.keys():
                res.extend([dic[nums[i]], i])
            else:
                r = target - nums[i]
                dic[r] = i
        
        return res