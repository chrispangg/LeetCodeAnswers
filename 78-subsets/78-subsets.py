"""
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(start):
            res.append(subset.copy())
            for i in range(len(nums))[start::]:
                subset.append(nums[i])
                dfs(i+1)
                subset.pop()

        dfs(0)
        return res 