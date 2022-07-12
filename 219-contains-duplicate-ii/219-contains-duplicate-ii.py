"""
Sliding Window: in the size of k
l, r = 0, 0 
use array to keep track
for loop to go forward
is it not set? 
    if it less than k? If yes, then add it in
    if it's not less than k, remove leftest value, then increment left
else: return True


if value r is not in array, remove the leftest value from the array
if value is in the array, return true

"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        l = 0
        numSet = set()
            
        for r in range(len(nums)):
            if nums[r] not in numSet:
                if r - l >= k:
                    numSet.remove(nums[l])
                    l += 1
                    
                numSet.add(nums[r])
            else:
                return True
                    
        return False
            