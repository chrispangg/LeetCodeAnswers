class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subset = []
        
        def backtrack(i):
            if sum(subset) == target and subset not in res:
                res.append(subset.copy())
                return
            if i >= len(candidates) or sum(subset) > target:
                return
            
            subset.append(candidates[i])
            backtrack(i + 1)
            
            subset.pop()
            if not subset or subset[-1] != candidates[i]:
                backtrack(i + 1)
            
        backtrack(0)
        return res
            
            