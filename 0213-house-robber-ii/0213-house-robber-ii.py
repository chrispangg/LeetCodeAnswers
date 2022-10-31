"""
if robbed the first house, then cannot rob the last house
if robbed the 2nd house, then can rob the last house

"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i, n):
            if i in dp: return dp[i]
            if i >= n: return 0
            dp[i] = max(nums[i] + dfs(i + 2, n), dfs(i + 1, n))
            return dp[i]
        r1 = dfs(0, len(nums) - 1)
        dp = {}
        r2 = dfs(1, len(nums))
        return max(nums[0], r1, r2)
    
            
            