class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def quicksort(nums):
            if len(nums) <= 1:
                return nums
            
            pivot = nums[0]
            less = [i for i in nums[1:] if i <= pivot]
            greater = [i for i in nums[1:] if i > pivot]
            
            return quicksort(less) + [pivot] + quicksort(greater)
        
        arr = quicksort(nums)
        print(arr)
        return arr[-k]
            
            