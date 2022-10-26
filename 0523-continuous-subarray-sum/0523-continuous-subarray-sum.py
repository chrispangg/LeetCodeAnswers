class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic = {0: -1} #remainder:Index
        total = 0
        for i, num in enumerate(nums):
            total += num
            r = total % k
            if r not in dic:
                dic[r] = i
            
            elif i - dic[r] >= 2:
                return True

        return False