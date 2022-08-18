class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subset = []
        
        def backtrack(i):
            # success base case
            if sum(subset) == target:
                res.append(subset[:])
            # failed base case
            if i >= len(candidates) or sum(subset) >= target:
                return
            
            subset.append(candidates[i])
            backtrack(i + 1)
            
            subset.pop()
            
            while i < len(candidates) - 1 and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i + 1)
            
        backtrack(0)
        return res