class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        one, two = 2, 1
        
        for i in range(n-2):
            temp = one
            one = one + two
            two = temp
        return one