"""



"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        subset = []
        
        def backtrack(i):
            #base case:            
            if i >= len(nums):
                subsetCopy = subset.copy()
                subsetCopy.sort()
                res.add(tuple(subsetCopy))
                return
            #to include nums[i]
            subset.append(nums[i]) 
            backtrack(i + 1)
            
            subset.pop()
            backtrack(i + 1)
        
        backtrack(0)
        return res