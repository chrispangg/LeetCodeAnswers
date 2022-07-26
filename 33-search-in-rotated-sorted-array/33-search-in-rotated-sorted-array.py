class Solution:
    def search(self, nums: List[int], target: int) -> int:
            
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            
            if nums[m] == target:
                return m
            
            # left side is sorted
            if nums[l] <= nums[m]:
                # when target is within the left range
                if target < nums[m] and nums[l] <= target:
                    r = m - 1
                else: # or target > nums[m] or target < nums[l]
                    l = m + 1    
            # right side is sorted
            else:
                # when target is within the right range
                if nums[m] < target and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            
        return -1