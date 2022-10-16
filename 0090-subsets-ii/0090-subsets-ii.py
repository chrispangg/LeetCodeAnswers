class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []
        subset = []
        
        def backtrack(i):
            if i == len(nums):
                subsets.append(subset[:])
                return
            
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()
            while i < len(nums) - 1 and nums[i] == nums[i+1]:
                i += 1
            backtrack(i + 1)
            
        backtrack(0)
        return subsets