class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = {i for i in range(len(nums) + 1)}
        for i in res:
            if i not in nums:
                return i