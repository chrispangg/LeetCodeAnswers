class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r)//2
            if nums[l] <= nums[m]:
                if nums[l] > nums[r]:
                    l = m + 1
                else:
                    return nums[l]
            else: 
                
                if m - 1 >= 0:
                    r = m
                else:
                    l = m
                        
        return nums[m]