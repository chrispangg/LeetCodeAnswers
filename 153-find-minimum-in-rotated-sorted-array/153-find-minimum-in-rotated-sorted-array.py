class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        res = nums[0]
        l, r = 0, len(nums) - 1
        
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            else:
                m = (l + r)//2
                res = min(res, nums[m])
                
                #If left is sorted, then move pointer to right side
                if nums[m] >= nums[l]:
                    l = m + 1
                else: # If right is sorted, then search left
                    r = m - 1
                
        return res