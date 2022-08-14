# Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3] output = 3
# use a monotonic increasing stack

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        
        stack = []
        for p, s in sorted(pairs)[::-1]:
            time = (target - p) / s
            stack.append(time)
            print(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                
        return len(stack)
            