"""
Use a queue:
    1. check if nums[r] is greater than the top value of the queue (queue[-1]). If it is we queue.pop() until nums[r] is no longer greater than queue[-1]
    1. add nums[r] to the queue to the right side
    2. remove nums[l] from the left of the queue if num[l] is at queue[0] or if value 
    3. remove value less than or equal to the lesftest value in the queue (using a while loop) and len(queue) != 1
    4. if r+1 - l == k, add leftest value from queue to res

"""

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque([])
        res = []
        l = 0
        
        for r in range (len(nums)):
            #pop smaller values from queue
            while queue and nums[r] > nums[queue[-1]]:
                queue.pop()
            
            #append value to the right of queue
            queue.append(r)    
            
            #remove left val from window
            if l - 1 == queue[0]:
                queue.popleft()
                
            if r + 1 >= k:
                res.append(nums[queue[0]]) 
                l += 1
        
        return res