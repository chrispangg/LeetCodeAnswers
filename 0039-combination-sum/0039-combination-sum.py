class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(i, nums):
            if sum(nums) == target:
                res.append(tuple(nums))
                return 
            if sum(nums) > target or i == len(candidates):
                return
            
            nums.append(candidates[i])
            
            dfs(i, nums)
            nums.pop()
            dfs(i + 1, nums)
            
        dfs(0, [])
        
        return res
            
            
            