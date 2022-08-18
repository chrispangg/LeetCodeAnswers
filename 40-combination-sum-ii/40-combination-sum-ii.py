class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subsets = []
        
        def backtrack(pos, target):
            if target == 0:
                res.append(subsets[:])
            if target <= 0:
                return
            
            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                subsets.append(candidates[i])
                backtrack(i + 1, target - candidates[i])
                subsets.pop()
                
                prev = candidates[i]
            
        backtrack(0, target)
        return res