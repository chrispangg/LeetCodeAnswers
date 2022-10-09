class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        target = sum([i for i in range(len(nums) + 1)])
        total = sum([i for i in nums])
        return target - total