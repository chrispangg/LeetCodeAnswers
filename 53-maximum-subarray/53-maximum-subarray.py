class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, total = nums[0], 0
        for n in nums:
            if total < 0: total = 0
            total += n
            res = max(res, total)
        return res