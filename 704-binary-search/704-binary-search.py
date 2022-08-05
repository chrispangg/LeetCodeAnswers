class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        
        while l < r:
            m = (r + l) // 2
            if nums[m] < target:
                l = m + 1 # +1 to exlude m in the next loop
            elif nums[m] > target:
                r = m # -1 to exclude m in the next loop
            else:
                return m
        return -1