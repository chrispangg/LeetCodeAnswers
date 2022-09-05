class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 2, 1
        if n == 1: return two
        if n == 2: return one
        for i in range(n-2):
            temp = one
            one = one + two
            two = temp
        return one