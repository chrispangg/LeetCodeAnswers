class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2: return False
        
        target = sum(nums) / 2
        cache = {0}
        for n in nums:
            for c in cache.copy():
                if n + c == target: return True
                else: cache.add(n + c)
        return False