class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, subset = [], []
        
        def backtrack(i):
            #base case
            if i == len(nums):
                res.append(subset[:])
                return
            
            # All subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()
            
            #All subsets that don't include nums[i]
            # while inbound and the next value is not a duplicate
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)
            
        backtrack(0)
        return res
        