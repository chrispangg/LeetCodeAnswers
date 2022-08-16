class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, subset):
            if sum(subset) == target:
                res.append(subset.copy())
                return
            if i >= len(candidates) or sum(subset) > target:
                return

            subset.append(candidates[i])
            backtrack(i, subset)
            subset.pop()
            backtrack(i + 1, subset)


        backtrack(0, [])
        return res