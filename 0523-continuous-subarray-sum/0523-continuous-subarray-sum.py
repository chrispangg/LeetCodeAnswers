class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic = {0: -1} #remainder:Index
        total = 0
        for i, num in enumerate(nums):
            total += num
            remainder = total % k
            if remainder not in dic:
                dic[remainder] = i
            
            elif  i - dic[remainder] > 1:
                return True

        return False
            
            
            