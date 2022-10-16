class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (r + l) // 2
            
            if nums[m] == target:
                return m
            elif nums[l] <= nums[m]: #left side in order
                if nums[l] <= target < nums[m]: #within the left side
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] <= nums[r]: #right side in order
                if nums[m] < target <= nums[r]: # in the rigth side
                    l = m + 1
                else:
                    r = m - 1
            
        return -1