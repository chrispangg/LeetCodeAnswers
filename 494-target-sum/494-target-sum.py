class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
    
        def dfs(i, total):
            if i == len(nums):
                return 1 if total == target else 0

            if (abs(i), total) in cache: 
                return cache[(i, total)]
            
            cache[(i, total)] = dfs(i+1, (total + nums[i])) + dfs(i+1, (total - nums[i]))
            return cache[(i, total)]


        return dfs(0, 0)