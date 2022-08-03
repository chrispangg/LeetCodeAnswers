class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        # Look for the start of the loop i.e. where fast and slow meet
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # start another slow pointer (slow2) from the beginning
        # because the distance between the starting position and the start of the cycle is equal 
        # to the distance between the slow and fast pointer and the start of the position
        # when the meet, we know that's the duplicate
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow