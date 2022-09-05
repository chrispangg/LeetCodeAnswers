class Solution:
    def climbStairs(self, n: int) -> int:
        curr, one, two = 0, 1, 2
        
        for i in range(n-1):
            curr = one + two
            one = two
            two = curr
        
        return one