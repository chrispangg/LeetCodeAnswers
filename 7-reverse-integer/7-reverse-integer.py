class Solution:
    def reverse(self, x: int) -> int:
        reversedR = int(str(abs(x))[::-1])
        if reversedR > 2147483647: return 0
        return reversedR * -1 if x < 0 else reversedR