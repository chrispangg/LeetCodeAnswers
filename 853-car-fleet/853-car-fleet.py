class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position, speed)] #create an array of [pos, speed] pairs
        
        stack = []
        for p, s in sorted(pair)[::-1]: #Reverse Sorted Order
            time = (target - p) / s
            stack.append(time)
            #if the car we appended stack[-1] will take less time than the car before stack[-2],
            # then we know it will catch up, and thus it will merge with stack[-1].
            # So we can remove it from top of stack (as it is now merged with stack[-1])
            if len(stack) >= 2 and stack[-1] <= stack[-2]: 
                stack.pop()
        
        return len(stack)