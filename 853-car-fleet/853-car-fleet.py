# Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3] output = 3
# use a monotonic increasing stack

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        
        stack = []
        for p, s in sorted(pairs)[::-1]:
            time = (target - p) / s
                
            if len(stack) < 1 or len(stack) >= 1 and time > stack[-1]:
                stack.append(time)
                
        return len(stack)
            