class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        subsets = []
        subset = []
        
        def dfs(i):
            if sum(subset) == target:
                subsets.append(subset.copy())
                return
            if i == len(candidates) or sum(subset) > target:
                return
            
            subset.append(candidates[i])
            dfs(i + 1)
            subset.pop()
            
            while i < len(candidates) - 1 and candidates[i] == candidates[i+1]:
                i+= 1
            dfs(i + 1)
                       
        dfs(0)
        return subsets
            