# Solution: QuickSelect
# Time Complexity: 
#   - Best Case: O(n)
#   - Average Case: O(n)
#   - Worst Case: O(n^2)
# Extra Space Complexity: O(1)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k #index we are looking for after sorted
        
        def quickSelect(l, r):
            # partition
            p, pivot = l, nums[r]
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
                    
            nums[p], nums[r] = nums[r], nums[p]
            
            if p > k: # meaning k is in left side
                return quickSelect(l, p - 1)
            if p < k: # meaning k is in the right side
                return quickSelect(p + 1, r)
            else:
                return nums[p]
            
            
        return quickSelect(0, len(nums) - 1)