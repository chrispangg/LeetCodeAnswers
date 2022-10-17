class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs():
            if len(subset) == len(nums):
                res.append(subset[:])
                return 
            for i in nums:
                if i not in subset:
                    subset.append(i)
                    dfs()
                    subset.pop()

            
        dfs()
        return res