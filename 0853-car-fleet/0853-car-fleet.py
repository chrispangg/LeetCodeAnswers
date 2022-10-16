class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(list(zip(position, speed)))[::-1]
        stack = [float('-inf')]
        for pos, speed in pairs:
            steps = (target - pos) / speed
            stack.append(steps)
            if stack[-1] <= stack[-2]: #meaning prev can catchup
                stack.pop()
        
        return len(stack) - 1