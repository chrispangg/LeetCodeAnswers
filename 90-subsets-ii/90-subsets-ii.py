class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        subset = []
        
        def backtrack(i):
            #base case:            
            if i == len(nums):
                res.add(tuple(subset))
                return
            
            #to include nums[i]
            subset.append(nums[i])
            backtrack(i + 1)
            #to include nums[i]
            subset.pop()
            backtrack(i + 1)
        
        backtrack(0)
        return res