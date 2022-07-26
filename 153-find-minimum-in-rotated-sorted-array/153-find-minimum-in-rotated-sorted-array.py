class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r)//2
                
            # If left side is sorted, then nums[l] must be the smallest value on left side
            # If nums[l] > nums[r] then we can remove left side
            if nums[l] <= nums[m]:
                if nums[l] > nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else: 
                # If right side is sorted, then nums[m] must be the smallest value on right side
                if m - 1 >= 0:
                    r = m
                else:
                    l = m
                        
        return nums[m]
            
        