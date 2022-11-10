class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float("-inf")
        currMax, currMin = 1, 1
        for n in nums:
            temp = n * currMax
            currMax = max(n, temp, n*currMin)
            currMin = min(n, temp, n*currMin)
            res = max(currMax, res)
        return res
            
        